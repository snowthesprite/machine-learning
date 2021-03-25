import csv
class DataFrame :
    def __init__(self, input_dict, column_order) :
        self.data_dict = input_dict
        self.columns = column_order
    
    def to_array(self) :
        length_of_data = len(self.data_dict[self.columns[0]])
        data_array = [[] for _ in range(length_of_data)]
        for row in range(length_of_data) :
            for col_name in self.columns :
                data_array[row].append(self.data_dict[col_name][row])
        return data_array

    def select_columns(self, input_columns) :
        new_df = {key : self.data_dict[key] for key in input_columns}
        return DataFrame(new_df, input_columns)

    def select_rows(self, input_rows) :
        new_df = {}
        self_array = self.to_array()
        for col_name in self.columns :
            new_col_value = []
            for row_key in input_rows :
                new_col_value.append(self.data_dict[col_name][row_key])
            new_df[col_name] = new_col_value
        return DataFrame(new_df, self.columns)
            
    def apply(self, wanted_col, funct, new_name = None) :
        new_df = {}
        new_columns = [col if (col != wanted_col or new_name == None) else new_name for col in self.columns ]
        for col in self.columns :
            col_value = []
            for row_val in self.data_dict[col] :
                if col == wanted_col :
                    col_value.append(funct(row_val))
                else :
                    col_value.append(row_val)
            if new_name == None or col != wanted_col :
                new_df[col] = col_value
            else :
                new_df[new_name] = col_value
        return DataFrame(new_df, new_columns)

    @classmethod 
    def from_array(self, arr, columns) :
        new_df = {}
        for key_number in range(len(columns)) :
            key_data = []
            for row_index in range(len(arr)) :
                key_data.append(arr[row_index][key_number])
            new_df[columns[key_number]] = key_data
        return DataFrame(new_df, columns)

    def row_to_dict(self, row) :
        arr = self.to_array()
        new_dict = {}
        for col_index in range(len(self.columns)) :
            new_dict[self.columns[col_index]] = arr[row][col_index]
        return new_dict

    def select_rows_where(self, need) :
        arr = self.to_array()
        new_df = {name : [] for name in self.columns}
        for row_index in range(len(arr)) :
            row = self.row_to_dict(row_index)
            if need(row) :
                for key, value in row.items() :
                    new_df[key].append(value)
        return DataFrame(new_df, self.columns)

    def order_by(self, order, ascending = True) :
        if type(ascending) == str and ascending.casefold() == 'asc' :
            ascending = True
        elif type(ascending) == str and ascending.casefold() == 'desc' :
            ascending = False
        arr = self.to_array()
        location = self.columns.index(order)
        kind = False
        if type(self.data_dict[order][0]) == int :
            kind = True
        data_array = []
        for row in arr :
            if kind :
                num = row[location]
            else :
                num = row[location][0]
            run = False
            for i in range(-len(data_array),0) :
                if kind : 
                    compare = num < data_array[i][location]
                else :
                    index = 0
                    while index < len(row[location]) and index < len(data_array[i][location]) :
                        char_1 = row[location][index]
                        char_2 = data_array[i][location][index]
                        #print(row[location], data_array[i][location])
                       # print(char_1, char_2)
                        if char_1 != char_2 :
                            compare = char_1 < char_2
                            break
                        index+=1
                if compare :
                    data_array.insert(i, row)
                    run = True
                    break
            if not run :
                data_array.append(row)
        if not ascending :
            data_array.reverse()
        return DataFrame.from_array(data_array, self.columns)
        
    @classmethod
    def from_csv(self, path_to_csv, header = True, data_types = {}, parser = None) :
        all_rows = []
        with open(path_to_csv, "r") as file:
            if parser == None :
                data = csv.reader(file, quotechar='|', skipinitialspace = True)
            else :
                data = csv.reader(file, quotechar='|', skipinitialspace = True, delimiter = '\t')
            for row in data :
                if parser == None :
                    all_rows.append(row)
                else :
                    all_rows.append(parser(row[0]))
        all_rows.pop(len(all_rows) - 1)
        if header :
            key_names = all_rows[0]
        else :
            key_names = [str(col_num) for col_num in range(len(all_rows[0]))]
        all_rows.pop(0)
        new_df = {}
        for key in key_names :
            index = key_names.index(key)
            if key in data_types :
                key_type = data_types[key]
            else :
                key_type = (lambda a : a)
            key_data = []
            ''''
            for row in all_rows :
                #print(row)
                #if (key_type == int or key_type == float) and row[index] == '' : 
                if row[index] == '' :
                    key_data.append(None)
                else :
                    key_data.append(key_type(row[index]))
            #'''
            key_data = [None if row[index] == '' else key_type(row[index]) for row in all_rows]
            new_df[key] = key_data

        return DataFrame(new_df, key_names)

    def create_interaction_terms(self, col_1, col_2) :
        interaction_key = col_1 + " * " + col_2
        col_1_vals = self.data_dict[col_1]
        col_2_vals = self.data_dict[col_2]
        interaction_value = [col_1_vals[index] * col_2_vals[index] for index in range(len(col_1_vals))]
        new_data_dict = self.data_dict.copy()
        new_data_dict[interaction_key] = interaction_value
        new_columns = self.columns.copy()
        new_columns.append(interaction_key)
        return DataFrame(new_data_dict, new_columns)

    def create_dummy_variables(self, initial_key) :
        dummy_dict = {}
        for data_list in self.data_dict[initial_key] :
            for dummy_var in data_list :
                dummy_dict[dummy_var] = []
        dummy_keys = [key for key in dummy_dict]
        dummy_keys.reverse()
        for data_list in self.data_dict[initial_key] :
            for key in dummy_keys :
                if key not in data_list :
                    dummy_dict[key].append(0)
                else :
                    dummy_dict[key].append(1)

        new_data_dict = {key : self.data_dict[key] for key in self.data_dict if key != initial_key}
        inital_index = self.columns.index(initial_key)
        new_columns = [key for key in self.data_dict if key != initial_key]
        
        for dummy_key in dummy_keys :
            new_data_dict[dummy_key] = dummy_dict[dummy_key]
            new_columns.insert(inital_index, dummy_key)
        return DataFrame(new_data_dict, new_columns)

    def add_data(self, key, data, new_loc = 999) : 
        new_data_dict = self.data_dict.copy()
        new_columns = self.columns.copy()
        new_data_dict[key] = data
        new_columns.insert(new_loc, key)
        return DataFrame(new_data_dict, new_columns)

    def group_by(self, catagory, sub = None) :
        sorted_cata = list({element : [] for element in self.data_dict[catagory]}.keys())
        new_df = {col : [] for col in self.columns}
        new_df[catagory] = sorted_cata
        if sub != None :
            new_df[catagory] = list(sub)
        for element in new_df[catagory] :
            require = (lambda a : a[catagory] == element)
            if sub != None :
                print(element)
                require = sub[element]
            #print(element)
            where = self.select_rows_where(require).data_dict
            for col in self.columns :
                if col == catagory :
                    continue
                new_df[col].append(where[col])
        return DataFrame(new_df, self.columns)

    def aggregate(self, colname, how, new_name = None) :
        df_array = self.to_array()
        df_columns = self.columns.copy()
        col_index = self.columns.index(colname)

        hows = {'count' : (lambda a : len(a) if type(a) == list else 0), 
                'min' : (lambda a : min(a) if type(a) == list else None),
                'max' : (lambda a : max(a) if type(a) == list else None),
                'sum' : (lambda a : sum(a) if type(a) == list else a),
                'avg' : (lambda a : (sum(a)/len(a)) if type(a) == list and len(a) != 0 else 0)}
        
        for row_index in range(len(df_array)) :
            #new_val = how_funct(df_array[row_index][col_index])
            new_val = hows[how](df_array[row_index][col_index])
            df_array[row_index][col_index] = new_val
        if new_name != None :
            df_columns[col_index] = new_name
        
        return DataFrame.from_array(df_array, df_columns)
    
    def query(self, query) :
        split_query = [word.replace(',','') if ',' in word else word  for word in query.split(' ')]

        if split_query[0] != 'SELECT' :
            print('Unknown command')
            return

        queries = {'SELECT' : (lambda a,b,c : a.select_columns(split_query[b:c])),
                   'ORDER_BY' : (lambda a, b, c : a.order_by(split_query[b-2],split_query[c-1]))}

        query_order = [['SELECT',0,len(split_query),(None,None,True)]]

        if 'ORDER BY' in query :
            split_query.insert(split_query.index('ORDER'), 'ORDER BY')
            split_query.remove('ORDER')
            split_query.remove('BY')
            query_order.insert(0,['ORDER_BY',split_query.index('ORDER BY'), len(split_query), (-2, True,False)])
            query_order = self.sort_queries(query_order)

        df = DataFrame(self.data_dict, self.columns)
        for (query_name, start, stop, loop_controls) in query_order :
            start = start+1
            if loop_controls[2] : 
                df = queries[query_name](df, start, stop)
                continue
            if loop_controls[1] :
                start, stop = stop, start
            for index in range(start, stop, loop_controls[0]) :
                df = queries[query_name](df, index, index)
        
        return df

    def sort_queries(self, query_order) :
        new_order = []
        for (query, start, stop, loop_controls) in query_order :
            current_stop = stop
            for (_, start_2, __, ___) in query_order :
                if current_stop > start_2 and start < start_2 :
                    current_stop = start_2
            new_order.append([query, start, current_stop, loop_controls])
        return new_order


