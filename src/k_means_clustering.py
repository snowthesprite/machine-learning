import math
#probs gonna have to change. Buuuuuuuuuut this makes it an imput starting stuff
class KMeans () :
    def __init__ (self, starting_clusters, data) :
        self.clusters = starting_clusters
        self.data_arr = data
        self.clust_id = [id for id in self.clusters]
        self.center_dist = None

    def compute_center_dist (self) :
        center_dist = {id : [] for id in self.clust_id}
        
        for cluster_id in self.clust_id :
            for col_id in range(len(self.data_arr[0])) :
                col_mean = 0
                for node in self.clusters[cluster_id] :
                    col_mean += self.data_arr[node][col_id]
                col_mean = col_mean/len(self.clusters[cluster_id])
                center_dist[cluster_id].append(col_mean)
        self.center_dist = center_dist
    
    def compute_distances (self, node_id) :
        node_data = self.data_arr[node_id]
        node_dist = {}
        for cluster_id in self.clust_id :
            cluster = self.center_dist[cluster_id]
            euc_dist = 0
            for col_id in range(len(node_data)) :
                euc_dist += (cluster[col_id] - node_data[col_id]) ** 2
            euc_dist = math.sqrt(euc_dist)
            node_dist[cluster_id] = euc_dist
        return node_dist

    def update_clusters (self) :
        new_clusters = {id : [] for id in self.clust_id}
        self.compute_center_dist()
        for node_id in range(len(self.data_arr)) :
            node_dists = self.compute_distances(node_id)
            closest_center = (self.clust_id[0],node_dists[self.clust_id[0]])
            for (cluster_id, dist) in node_dists.items() :
                if dist < closest_center[1] :
                    closest_center = (cluster_id, dist)
            new_clusters[closest_center[0]].append(node_id)
        self.clusters = new_clusters

    def run (self) :
        while True :
            old_cluster = self.clusters
            self.update_clusters()
            if self.clusters == old_cluster :
                break
    
    def compute_square_error (self) : 
        total_error = 0
        for cluster_id in self.clust_id :
            center = self.center_dist[cluster_id]
            for node_id in self.clusters[cluster_id] :
                node = self.data_arr[node_id]
                error = 0
                for col_id in range(len(self.data_arr[0])) :
                    error += (node[col_id] - center[col_id]) ** 2
                total_error+= error
        return total_error


