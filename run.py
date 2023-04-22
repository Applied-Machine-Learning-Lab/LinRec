# from recbole.quick_start.quick_start import run_recbole

parameter_dict = {
   # 'neg_sampling': {'popularity': 100},
   'learning_rate': 0.001,    #0.001
   #'weight_decay': 0.01,
   'train_batch_size': 2048,   #512 for gowalla
   'eval_batch_size': 2048,    
   'train_neg_sample_args': None,   #
   'neg_sampling': None,
   'mask_ratio': 0.2,
   'hidden_size': 256,
   'inner_size': 256,
   'n_layers': 2,
   'n_heads': 8,
   'hidden_dropout_prob': 0.2,
   'attn_dropout_prob': 0.2,
   'hidden_act': 'gelu',
   'layer_norm_eps': 1e-12,
   'initializer_range': 0.02,
   # 'loss_type': 'CE',
   # 'eval_args': {'split': {'LS': 'valid_and_test'}, 'order': 'TO', 'mode': 'pop100', 'group_by': 'user'},
   'topk': 10,
   'metrics': ['Recall', 'MRR', 'NDCG'],
   'valid_metric': 'NDCG@10'
}
# print(run_recbole(model='BERT4Rec', dataset='gowalla-merged', config_file_list=['gowalla.yaml'], config_dict=parameter_dict))
run_recbole(model='SASRec', dataset='ML-1M', config_dict=parameter_dict)


# FDSA, SASRecF
# from recbole.quick_start import run_recbole
# parameter_dict = {
#       # 'neg_sampling': {'popularity': 100},
#    'learning_rate': 0.001,    #0.001
#    #'weight_decay': 0.01,
#    'train_batch_size': 1024,   #2048
#    'eval_batch_size': 1024,   #2048 
#    'neg_sampling': None,
#    'mask_ratio': 0.2,
#    'hidden_size': 64,   #128
#    'inner_size': 256,
#    'n_layers': 2,
#    'n_heads': 8,
#    'hidden_dropout_prob': 0.2,
#    'attn_dropout_prob': 0.2,
#    'hidden_act': 'gelu',
#    'layer_norm_eps': 1e-12,
#    'initializer_range': 0.02,
#    # 'loss_type': 'CE',
#    # 'eval_args': {'split': {'LS': 'valid_and_test'}, 'order': 'TO', 'mode': 'pop100', 'group_by': 'user'},
#    'topk': 10,
#    'metrics': ['Recall', 'MRR', 'NDCG'],
#    'valid_metric': 'NDCG@10',
#    'train_neg_sample_args': None,
#    # 'load_col':
#    #    {'inter': ['user_id', 'item_id', 'rating', 'timestamp'],
#    #    'item': ['item_id', 'genre']},
#    # 'selected_features': ['genre'],

#    # # gowalla
#    # 'load_col':
#    #    {'inter': ['user_id', 'item_id', 'rating', 'timestamp']},
#    # 'selected_features': ['item_id'],
# }
# run_recbole(model='SASRec', dataset='gowalla', config_dict=parameter_dict)

