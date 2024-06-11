from connect import *

def update_record():
    try:
        id_field = input("Enter the filmID of the record you want to update: ")

        dbCursor.execute("SELECT * from tblFilms where filmID = ?", (id_field,))

        a_record = dbCursor.fetchone()


        if a_record == None:
            print("Record doesn't exist")

        else:
            title = input("Enter film titile: ")
            yearReleased = input("Enter film year released: ")
            rating = input("Enter film rating: ")
            duration = input("Enter film duration: ")
            genre = input("Enter film genre: ")

            title = "'"+title+"'"
            yearReleased = "'"+yearReleased+"'"
            rating = "'"+rating+"'"
            duration = "'"+duration+"'"
            genre = "'"+genre+"'"

        dbCursor.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, Genre = ? WHERE filmID = {id_field}",(title,yearReleased,rating, duration, genre))
        db_con.commit()

    except sql.ProgrammingError as pe:
        print(f"Failed to execute: {pe}")

    finally:
        print("Process Complete")

if __name__ == "__main__":
    update_record()