import math

class KNearestNeighborsClassifier () :
    def __init__ (self, k) :
        self.number_k = k
        self.depend_var = None
        self.dataframe = None
    
    def fit (self, dataframe, dependent_variable) :
        self.dataframe = dataframe
        self.depend_var = dependent_variable
    
    def compute_distances (self, sample) :
        new_df = self.dataframe.copy()
        independ_vars = [var for var in list(new_df.columns) if var != self.depend_var]
        dist_data = []
        for index in range(new_df[self.depend_var].size) :
            distance = 0
            for var in independ_vars :
                distance += (new_df.to_dict()[var][index] - sample[var]) ** 2
            dist_data.append(math.sqrt(distance))
        new_df['Distance'] = dist_data
        return new_df

    def nearest_neighbors (self, sample) :
        sorted_df = self.compute_distances(sample)
        sorted_df = sorted_df.sort_values('Distance')
        sorted_df = sorted_df[['Distance', self.depend_var]]
        return sorted_df

    def classify (self, sample) :
        #This feels cluncked but yk im tired
        sorted_df = self.nearest_neighbors(sample)
        sorted_df = sorted_df[:self.number_k]
        sorted_dict = sorted_df.to_dict('list')
        counting_dict = {var : {'count' : 0, 'avg_dist' : 0} for var in sorted_dict[self.depend_var]}
        for index in range(sorted_df[self.depend_var].size) :
            key = sorted_dict[self.depend_var][index]
            counting_dict[key]['count'] += 1
            counting_dict[key]['avg_dist'] += sorted_dict['Distance'][index]
        highest_count = 0
        lowest_dist = 100000
        by_dist = False
        for var in counting_dict :
            section = counting_dict[var]
            section['avg_dist'] = section['avg_dist']/section['count']
            if section['count'] > highest_count :
                count_choice = var
                highest_count = section['count']
            elif section['count'] == highest_count :
                by_dist = True
            if section['avg_dist'] < lowest_dist :
                dist_choice = var
                lowest_dist = section['avg_dist']
        
        if by_dist :
            return dist_choice
        return count_choice

