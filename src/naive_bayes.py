class NaiveBayes () :
    def __init__(self, data) :
        self.data = data
        self.classes = ['scam', 'not']
        self.var = data.keys().remove('class')
        self.total =  len(data['class'])
        self.class_percent = self.calc_class_percent()
        self.var_class_percent = self.calc_var_class_percent()
    

    def calc_class_percent(self) :
        class_percent = {kind : 0 for kind in self.classes}
        for kind in self.classes :
            for element in self.data['class'] :
                if element == kind :
                    class_percent[kind] += 1
            class_percent[kind] = class_percent[kind]/self.total
        return class_percent


    def calc_var_class_percent(self) : 
        kind_totals = {kind: self.class_percent[kind]*self.total}
        var_class_percent = {kind : {var: {1:0} for var in self.var} for kind in self.kind}
        for col in range(self.total) :
            kind = data['class'][col]
            for var in self.var :
                var_class_percent[kind][var][data[var][col]] += 1/kind_totals[kind]

        return var_class_percent


    def chance_of_class(self, imput) :
        class_chance = {kind : self.class_percent[kind] for kind in self.classes}
        for kind in self.classes :
            for var in self.var :
                class_chance[kind] = class_chance[kind] * self.var_class_percent[kind][var][imput[var]]
        return class_chance


    def find_class(self, imputs) :
        pass