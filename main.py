from dbs_create import db_create
from raw_table1 import ds1_create
from raw_table2 import ds2_create
from raw_table_insert import ds1_insert
from raw_table_insert2 import ds2_insert
from raw_table_norm import ds1_norm
from raw_table_norm2 import ds2_norm
from dw import dw
from dw_insert import dw_insert
from trigger1 import ds_trigger1
from trigger2 import ds2_trigger


def main():
    
    db_create()
    ds1_create()
    ds2_create()
    ds1_insert()
    ds2_insert()
    ds1_norm()
    ds2_norm()
    ds_trigger1()
    ds2_trigger()
    dw()
    dw_insert()

if __name__ == "__main__":
    main()