from connect import *

def delete_record():
    try:
        id_field = input("Enter the filmID of the record you want to update: ")
        dbCursor.execute("SELECT * from tblFilms where filmID = ?", (id_field,))

        a_record = dbCursor.fetchone()


        if a_record == None:
            print("Record doesn't exist")

        else:
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (id_field,))
            db_con.commit()
            print(f"Record {id_field} deleted from table")
    except sql.ProgrammingError as pe:
        print(f"Failed to execute: {pe}")

    finally:
        print("Process Complete")



if __name__ == "__main__":
    delete_record()