import csv
class DataFrame :
    def __init__(self, imputed_dict, column_order) :
        self.data_dict = imputed_dict
        self.columns = column_order
    
    def to_array(self) :
        length_of_data = len(self.data_dict[self.columns[0]])
        data_array = [[] for _ in range(length_of_data)]
        for row in range(length_of_data) :
            for col_name in self.columns :
                data_array[row].append(self.data_dict[col_name][row])
        return data_array

    def select_columns(self, imput_columns) :
        new_df = {}
        for key in imput_columns :
            new_df[key] = self.data_dict[key]
        return DataFrame(new_df, imput_columns)

    def select_rows(self, imput_rows) :
        new_df = {}
        self_array = self.to_array()
        for col_name in self.columns :
            new_col_value = []
            for row_key in imput_rows :
                new_col_value.append(self.data_dict[col_name][row_key])
            new_df[col_name] = new_col_value
        return DataFrame(new_df, self.columns)
            
    def apply(self, wanted_col, funct) :
        new_df = {}
        for col in self.columns :
            col_value = []
            for row_val in self.data_dict[col] :
                if col == wanted_col :
                    col_value.append(funct(row_val))
                else :
                    col_value.append(row_val)
            new_df[col] = col_value
        return DataFrame(new_df, self.columns)

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

    def order_by(self, order, ascending) :
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
    def from_csv(self, path_to_csv, header) :
        all_rows = []
        with open(path_to_csv, "r") as file:
            data = csv.reader(file, quotechar='|', skipinitialspace = True)
            for row in data :
                all_rows.append(row)
        all_rows.pop(len(all_rows) - 1)
        if header == True :
            key_names = all_rows[0]
        all_rows.pop(0)
        new_df = {}
        for key in key_names :
            index = key_names.index(key)
            key_data = [row[index] for row in all_rows]
            new_df[key] = key_data
        return DataFrame(new_df, key_names)
