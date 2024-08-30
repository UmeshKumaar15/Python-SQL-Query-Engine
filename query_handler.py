#Database Query Handler

class SQL:

    def __init__(self):
        self.database = {}
        self.metadata = {}
        self.table_name = ""
        self.constraints = { "NOTNULL", "UNIQUE", "PRIMARY", "FOREIGN", "CHECK", "DEFAULT", "INT"}
        self.datatypes = {"VARCHAR"}

    def getQuery(self, query):
        query = query.upper()
        query = query.strip()
        query = query.replace(',', ' ')
        command = query.partition(' ')[0]

        if command == "CREATE":
            self.create_table(query)
        elif command == "INSERT":
            self.insert_into(query)
        elif command == "SELECT":
            self.select_from(query)
        elif command == "DESC":
            self.desc_table(query)
        elif command == "SHOW":
            self.display_db()
        
    def create_table(self, query):
        query = query.split()

        for word in range(len(query)):
            if query[word] == "TABLE":
                table_name = query[word+1]
                if table_name not in self.database:
                    self.database[table_name] = {}
                    self.metadata[table_name] = {}
                else:
                    raise Exception("Table name already exists")
            
            if query[word] in self.constraints:
                if table_name in self.database:
                    table = self.database[table_name]
                    if query[word] not in table:
                        table[query[word-1]] = []

                if table_name in self.metadata:
                    table = self.metadata[table_name]
                    if query[word-1] not in table:
                        table[query[word-1]] = query[word]
    
    def insert_into(self, query):
        query = query.split()
        flag = False
        value_arr = []
        for word in range(len(query)):

            if query[word] == ")":
                flag = False
            if query[word] == "INTO":
                table_name = query[word+1]
                self.table_name = table_name
           
            if flag:
                index = 0
                value_arr.append(query[word])
                index += 1
            if query[word] == "(":
                flag = True

        index = 0
        for key in list(self.database[self.table_name].keys()):
            self.database[self.table_name][key].append(value_arr[index])
            index += 1

    def select_from(self, query):
        query = query.split()
        display_parameters = []
        flag = False
        for word in range(len(query)):
            if query[word] == "FROM":
                self.table_name = query[word + 1]
        
        for word in range(len(query)):
            if query[word] == "FROM":
                flag = False
            if flag:
                display_parameters.append(query[word])
            if query[word] == "SELECT":
                if query[word+1] == "*":
                    self.display_table(self.table_name, display_parameters)
                else:
                    flag = True

        self.display_table(self.table_name, display_parameters)
        
    def desc_table(self, query):
        max_e = 0
        query = query.split()
        for word in range(len(query)):
            if query[word] == "DESC":
                table_name = query[word + 1]

        header = "Name          Constraint"
        print()
        print("Table: " , table_name)
        print("-------" + "-" * len(table_name))
        print()
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        keys = list(self.metadata[table_name])


        row_output = ""
        for key in keys:
            max_e = max(max_e, len(key))
        
        for key in keys:
            row_output = ""
            row_output = row_output + key + " " * (max_e+ (max_e-len(key))) + self.metadata[table_name][key]
            print(row_output)
        
    def display_db(self):
        print()
        print("-" * 8)
        print("DATABASE")
        print("-" * 8)
        print()

        tables = list(self.database.keys())
        for table in tables:
            print(table)
        
    def display_table(self, table_name, display):
        max_e = 0
        line_count = 0
        columns = ""
        if display == []:
            display = list(self.database[table_name].keys())
        for word in display:
            line_count = line_count + len(word) + 8
        for key in display:
            columns += key
            columns += "        "
        
        print()
        print("Table: " , table_name)
        print("-------" + "-" * len(table_name))
        print()
        print("-" * line_count)
        print(columns)
        print("-" * line_count)

        rows = len(self.database[table_name][display[0]])
        row_output = ""
        for i in range(rows):
            row_output = ""
            for key in display:
                max_e = max(len(self.database[table_name][key][i]), max_e)
            
            for key in display:
                elements = self.database[table_name][key][i]
                elements += " " * (max_e + (max_e - len(elements)))
                row_output += elements
            print(row_output)


if __name__ == "__main__":

    session = SQL()
    session.getQuery("create table student ( studentname NOTNULL VARCHAR2(25), ROLL_NO PRIMARY VARCHAR2(10), SCORE INT );")
    session.getQuery("create table employee ( empname NOTNULL VARCHAR2(25), empid PRIMARY VARCHAR2(10), Salary INT );")
    # print(session.metadata)
    print(session.metadata)
    session.getQuery("insert into student values ( umesh, 21BCE0493, 84 ) ;")
    session.getQuery("insert into student values ( mathava, er4gg, 44 ) ;")
    session.getQuery("insert into student values ( sanjith, 21BCE0039, 100 ) ;")
    session.getQuery("select * from student ;")
    session.getQuery("desc student ;")
    session.getQuery("show tables;")
