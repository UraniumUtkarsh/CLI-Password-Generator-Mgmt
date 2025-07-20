#June 18, 2021
#Like Search Feature

#Under Development - New Feature Search
def SearchLike():
    print(" Categories of Search~\n")
    print("""
    1. startswith
    2. ends-with
    3. is in middle at any position
    4. Value is in 2nd position
    5. Value that starts with any character of your choice and have atleast 2 characters in length
    6. Value that starts with any charcter of your choice and have at least 3 characters in lenth
    7. Value that starts with any character of your choice and ends with any other specific character

0. Return
    """)

def validate(field):
    _list = ['name','website','username','date']
    if (field in _list) == True:
        return 1
    else:
        return 0
    

class like:
    def field():
            
        print("""
        Fields Available~
            1. name
            2. website
            3. username
            4. date

    """)
        field = input("Input Field: ")
        return field
    
    def like1(where):
        valid=validate(where)
        if valid==0:
            return "Invalid"
        else:
            pass
        try:
            connection=co.connect(host="localhost",user="root",passwd="root",database="savedpasswords")
            cursor=connection.cursor()

            where_join = "SELECT * FROM data WHERE %s"%(where)

            starter = input("Starts-with letter: ")
            
            Like_join = where_join + " LIKE '%s%'"%(starter)

            sql=Like_join
            cursor.execute(sql)
            data=cursor.fetchall()

            for row in data:
                print(row)
                
            connection.close()
            return
        except:
            return False
