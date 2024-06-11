from connect import*

def add_record():
    try :

        title = input("Enter film titile: ")
        yearReleased = input("Enter film year released: ")
        rating = input("Enter film rating: ")
        duration = input("Enter film duration: ")
        genre = input("Enter film genre: ")



        dbCursor.execute("INSERT INTO tblFilms Values(null,?,?,?,?,?)",(title,yearReleased,rating, duration, genre))
        db_con.commit()
        print("Added song information.")
    except sql.ProgrammingError as pe:
        print(f"Failed to execute: {pe}")
    except sql.OperationalError as oe:
        print(f"Connection Faiel because {oe}")
    except sql.Error as e:
        print(f"Connection Faiel because {e}")
    finally:
        print("Operation Completed")

if __name__ == "__main__":
    add_record()