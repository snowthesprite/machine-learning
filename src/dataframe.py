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
        arr = self.to_array()
        location = self.columns.index(order)
        if type(self.data_dict[order][0]) == int :
            kind = True
        else:
            kind = False
        data_array = []
        for row in arr :
            if kind :
                num = row[location]
            else :
                num = row[location][0]
            i = -len(data_array)
            run = False
            while i < 0  :
                if kind :
                    compare = num < data_array[i][location]
                else :
                    compare = num < data_array[i][location][0]
                if compare and not run :
                    data_array.insert(i, row)
                    run = True
                i += 1
            if data_array == [] or not run :
                data_array.append(row)
        if not ascending :
            data_array_2 = []
            k = len(data_array) - 1
            while k >= 0 :
                data_array_2.append(data_array[k])
                k -= 1
            data_array = data_array_2
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

    def group_by(self, catagory) :
        sorted_cata = list({element : [] for element in self.data_dict[catagory]}.keys())
        new_df = {col : [] for col in self.columns}
        new_df[catagory] = sorted_cata
        for element in sorted_cata :
            require = (lambda a : a[catagory] == element)
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
        
        if how == 'count' :
            how_funct = (lambda a : len(a) if type(a) == list else 0)
        elif how == 'min' :
            how_funct = (lambda a : min(a) if type(a) == list else None)
        elif how == 'max' :
            how_funct = (lambda a : max(a) if type(a) == list else None)
        elif how == 'sum' :
            how_funct = (lambda a : sum(a) if type(a) == list else a)
        elif how == 'avg' :
            how_funct = (lambda a : (sum(a)/len(a)) if type(a) == list else a)
        else :
            print('Unknown command')
            return
        
        for row_index in range(len(df_array)) :
            new_val = how_funct(df_array[row_index][col_index])
            df_array[row_index][col_index] = new_val
        if new_name != None :
            df_columns[col_index] = new_name
        
        return DataFrame.from_array(df_array, df_columns)
    
    def query(self, query) :
        split_query = query.split(' ')
        for q_id in range(len(split_query)) :
            if ',' in split_query[q_id] :
                split_query[q_id] = split_query[q_id].replace(',','')
        if split_query[0] != 'SELECT' :
            print('Unknown command')
            return
        return self.select_columns(split_query[1:])
