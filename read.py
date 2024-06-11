from connect import*

def read_records():
    try:
        dbCursor.execute("Select*from tblFilms")
        
        
        all_records = dbCursor.fetchall()

        if all_records:


            for arecord in all_records:
                print(arecord)
            else :
                print("No records found in songs table.")
    except sql.ProgrammingError as pe: 
        print(f"Failed to execute: {pe}")

    finally:
        print("Process complete")

if __name__ == "__main__":
    read_records()