from connect import *

def search_report ():
    try:
        field = input("Would you like to search by FilmID, Title, Release_Year, Rating, Duration or Genre?: ")
        if field =="filmID":
            id_field = input("Enter the filmID of the record you want to update: ")
            dbCursor.execute("SELECT * from tblFilms where filmID = ?", (id_field,))

            a_record = dbCursor.fetchone()
            if a_record==None:
                print(f"The song with filmID {id_field} doesn't exist in the song table.")
            else:
                print(a_record)
        elif field == "Title" or field == "Release_Year" or field == "Rating" or field == "Duration" or field == "Genre":
            search_str= input (f"Enter the search criteria: ")
            dbCursor.execute(f"select * from tblFilms Where {field} like '%%{search_str    }'")

            search_record = dbCursor.fetchall()

            if search_record == None:
                print(f"The record with {field} matched with {search_str} in the song table.")
            else:
                for records in search_record:
                    print(records)
        else:
            print("Invalid Search Field!")
    except sql.ProgrammingError as pe:
        print(f"Failed to execute: {pe}")

    finally:
        print("Process Complete")



if __name__ == "__main__":
    search_report()