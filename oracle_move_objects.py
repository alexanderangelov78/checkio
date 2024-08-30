'''задаване на входни параметри - тейбълспейс нейм сорс и таргет, дф файл ид от дба дейта файлс , конекшън стринг

1 връзка към базата
	1.1селектиране на екстенд картата за файла
	1.2 запис във файл на екстенд картата

2 генериране и запис във файл на командите за местене (таблици и индекси)

3 агенериране на команди за лоб индекси и лоб сегменти записване във файл

4. изпълнение на лоб файловете

5. проверка на hwm

6. shrink na file-a '''

import cx_Oracle
import csv

FILE_ID = 9
EXTEND_MAP_FILE = f'HWM_file_id_{FILE_ID}.csv'
TABLESPACE_NAME_TARGET = 'WEXS_DATA'
PARALLEL_DEGREE = 4
MOVE_COMMANDS_LIST = []
MOVE_COMMANDS4LOBS_LIST = []
GET_LOBSEGMENTS_TABLES_SQL = [] # queries which prepares sqls to move the right index or table



def save_result2file(lines, file_name):
    #1.2 save result in csv
    with open(file_name, 'w') as f:
        #column headers
        f.write("file_id;sta;rtend;blocks;owner;segment_name;partition_name;object_type")
        f.write('\n')
        for tuple_line in lines:
            f.write(''.join(tuple_line))
            f.write('\n')


def save_commands2files(commandsList,ora_object_type):
    # saves sql commands for tables and indexes to move out to othere tablespace TABLESPACE_TARGET
    print(f"===creation of file_id_{FILE_ID}_move_{ora_object_type}.sql============= " )
    with open(f"file_id_{FILE_ID}_move_{ora_object_type}.sql", 'w') as f:
        for sql_command in commandsList:
            #print(sql_command)
            #print(type(sql_command))
            f.write(''.join(sql_command))
            f.write('\n')

def save_commands2files_lobs(commandsList,ora_object_type):
    # saves sql commands for tables and indexes to move out to othere tablespace TABLESPACE_TARGET
    print(f"===creation of file_id_{FILE_ID}_move_{ora_object_type}.sql============= " )
    with open(f"file_id_{FILE_ID}_move_{ora_object_type}.sql", 'w') as f:
        for sql_command in commandsList:
            if sql_command == []:
                pass
            else:
                #print(sql_command[0]) #take first element of the list, which is a tupple
                #print(type(sql_command))
                f.write(''.join(sql_command[0]))
                f.write('\n')

def get_extends_map():
    print("=======================start_get_extends_map===================")
    #todo 1  get map of the tablespace
    #todo 1.1 create connection to database and get extends map
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Wexlog\instantclient_19_16")
    encoding = 'UTF-8'
    #extend_map_query_test = "select instance_name from v$instance"
    extend_map_query_test = f"select file_id||';'||block_id||';'||end_block||';'||blocks||';'||owner||';'||segment_name||';'||partition_name||';'||segment_type\
    from (select\
                file_id,\
                block_id,\
                block_id + blocks - 1   end_block,\
                blocks,\
                owner,\
                segment_name,\
                partition_name,\
                segment_type\
       from\
               dba_extents\
       where\
               tablespace_name = upper('{TABLESPACE_NAME_TARGET}')\
               and file_id={FILE_ID}\
       union all\
       select\
               file_id,\
               block_id,\
               block_id + blocks - 1   end_block,\
               blocks,\
               'free'                  owner,\
               'free'                  segment_name,\
               null                    partition_name,\
               null                    segment_type\
       from\
               dba_free_space\
       where\
               tablespace_name = upper('{TABLESPACE_NAME_TARGET}')\
               and file_id={FILE_ID}\
       order by\
               1,2)"
    try:
        connection = cx_Oracle.connect(
            "wexvs4tl_e4u_run",
            "wexvs4tl_e4u_run",
            'frmlvwdf4782831.prg-dc.dhl.com:1521/e4udevlocal',
            encoding=encoding
        )
        get_sofia_sql = connection.cursor()
        get_sofia_sql.execute(extend_map_query_test)
        get_sofia_sql_iterator = get_sofia_sql.fetchall()
        #print(get_sofia_sql_iterator)
        #write output to a csv file
        save_result2file(get_sofia_sql_iterator,EXTEND_MAP_FILE)
    except cx_Oracle.Error as error:
        print(error)
    finally:
        # release the connection
        if connection:
            connection.close()
    print("=======================end_get_extends_map===================")
# extend_map_query = "set line 200 \
# set pages 50000 \
# set hea off \
# select file_id||';'||block_id||';'||end_block||';'||blocks||';'||owner||';'||segment_name||';'||partition_name||';'||segment_type\
# from (select\
#             file_id,\
#             block_id,\
#             block_id + blocks - 1   end_block,\
#             blocks,\
#             owner,\
#             segment_name,\
#             partition_name,\
#             segment_type\
#    from\
#            dba_extents\
#    where\
#            tablespace_name = upper('WEXS_DATA')\
#            and file_id=10\
#    union all\
#    select\
#            file_id,\
#            block_id,\
#            block_id + blocks - 1   end_block,\
#            blocks,\
#            'free'                  owner,\
#            'free'                  segment_name,\
#            null                    partition_name,\
#            null                    segment_type\
#    from\
#            dba_free_space\
#    where\
#            tablespace_name = upper('WEXS_DATA')\
#            and file_id=10\
#    order by\
#            1,2)"
# try:
#     # connect to paris
#     connection_PROD = cx_Oracle.connect(
#         "wexvs4tl_e4u_run",
#         "wexvs4tl_e4u_run",
#         'frmlvwdf4782831.prg-dc.dhl.com:1521/e4udevlocal',
#         encoding=encoding
#     )
#     connection_PROD.callTimeout = 1700000
#     get_extend_map = connection_PROD.cursor()
#     get_extend_map.execute(extend_map_query)
#     extend_map_data = get_extend_map.fetchall()
#     #todo 1.1.2 write data in a file
#
# except cx_Oracle.Error as error:
#     print(error)
# finally:
#     connection_PROD.close()
#     # release the connection
#     if connection_PROD:
#         pass

def create_commands4move():
    #todo 2 split objects ; prepare sql for tables, indexes, Lobsegments & Lobindexes

    with open(EXTEND_MAP_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[7] == 'TABLE':
                    #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    #print(f'ALTER TABLE {row[5]} MOVE ONLINE TABLESPACE {TABLESPACE_NAME_TARGET}')
                    #alter table hr.employees move tablespace users online parallel 16;
                    MOVE_COMMANDS_LIST.append(f'ALTER TABLE {row[4]}.{row[5]} MOVE TABLESPACE {TABLESPACE_NAME_TARGET} ONLINE PARALLEL {PARALLEL_DEGREE};')
                    line_count += 1
                elif row[7] == 'INDEX':
                    #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    #ALTER INDEX <VS_CUSTCLEAR_BROKERFK_IDX> REBUILD TABLESPACE <WEXS_DATA_IND> ONLINE PARALLEL <4>
                    #print(f'ALTER INDEX {row[5]} REBUILD TABLESPACE {TABLESPACE_NAME_TARGET} ONLINE PARALLEL {PARALLEL_DEGREE};')
                    MOVE_COMMANDS_LIST.append(f'ALTER INDEX {row[4]}.{row[5]} REBUILD TABLESPACE {TABLESPACE_NAME_TARGET} ONLINE PARALLEL {PARALLEL_DEGREE};')
                    line_count += 1
                elif row[7] == 'LOBSEGMENT' or row[7] == 'LOBINDEX':
                    GET_LOBSEGMENTS_TABLES_SQL.append(f"select 'alter table {row[4]}.'||table_name||' move tablespace {TABLESPACE_NAME_TARGET} online' from (select * from dba_lobs where segment_name='{row[5]}')")
                    line_count += 1
                else:
                    line_count += 1
        print(f'Processed {line_count} lines.')
        #  2.1  create a file for tables and indexes
        #print(len(set(MOVE_COMMANDS_LIST)))
        #for el in set(MOVE_COMMANDS_LIST):
            #print(el)
        save_commands2files(MOVE_COMMANDS_LIST,"IND_and_TABS")
        # todo 3  create a file for output for lobsegments
        # 3 generate sql queries for move
        create_lob_sqls()


def create_lob_sqls():
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Wexlog\instantclient_19_16")
    for lob in (set(GET_LOBSEGMENTS_TABLES_SQL)):
        # execute each lob and result add to Lobs_file a
        encoding = 'UTF-8'
        #print(lob)
        try:
            connection_lob = cx_Oracle.connect(
                "wexvs4tl_e4u_run",
                "wexvs4tl_e4u_run",
                'frmlvwdf4782831.prg-dc.dhl.com:1521/e4udevlocal',
                encoding=encoding
            )
            get_lob_sql = connection_lob.cursor()
            get_lob_sql.execute(lob)
            get_lob_sql_iterator = get_lob_sql.fetchall()
            #print(get_lob_sql_iterator)
            #print(type(get_lob_sql_iterator))
            MOVE_COMMANDS4LOBS_LIST.append(get_lob_sql_iterator)
            # write output to a csv file

        except cx_Oracle.Error as error:
            print(error)
        finally:
            # release the connection
            if connection_lob:
                connection_lob.close()
    save_commands2files_lobs(MOVE_COMMANDS4LOBS_LIST, "LOBS")









#todo 4 execute queries with steps of 1G

# 1 връзка към базата
get_extends_map()

# 2 генериране и запис във файл на командите за местене
create_commands4move()


