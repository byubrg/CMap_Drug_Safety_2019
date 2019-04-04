import learner_functions as lf
import load_data as ld
import feature_selection as fs

data = ld.LoadData()

#create test and train labels
A375_culture_labels = data.A375_info['culture_id'].tolist()
A375_dili_labels = data.A375_info['DILIconcern'].tolist()

A375_expression_set = fs.univariate(data.A375_expression, A375_dili_labels)

knn_params = {
    "n_neighbors": 11
}

# train models
lf.train_rf(data.train_all.fillna(0), data.mislabel_labels)

knn_A375, knn_A375_score = lf.train_knn(A375_expression_set, A375_dili_labels, **knn_params)
