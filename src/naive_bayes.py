class NaiveBayes () :
    def __init__(self, data) :
        self.data = data
        self.classes = ['scam', 'not']
        self.var = list(data.keys())
        self.var.remove('class')
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
        kind_totals = {kind: self.class_percent[kind]*self.total for kind in self.classes}
        var_class_percent = {}
        for kind in self.classes :
            var_class_percent[kind] = {var : {1:0, 0:0} for var in self.var}
        print(kind_totals)
        for col in range(self.total) :
            kind = self.data['class'][col]
            for var in self.var :
                var_class_percent[kind][var][self.data[var][col]] += 1/kind_totals[kind]

        return var_class_percent


    def chance_of_class(self, imput) :
        class_chance = {kind : self.class_percent[kind] for kind in self.classes}
        for kind in self.classes :
            for var in self.var :
                class_chance[kind] = class_chance[kind] * self.var_class_percent[kind][var][imput[var]]
        return class_chance


    def find_class(self, imput) :
        chances = self.chance_of_class(imput)
        #print(chances)
        class_kind = None
        class_chance = 0
        for (kind, percent) in chances.items() :
            if percent > class_chance :
                class_chance = percent
                class_kind = kind
        return class_kind