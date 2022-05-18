import argparse


def arg_parse():
    parser = argparse.ArgumentParser()

    hparams = parser.add_argument_group('hyper-parameters')
    options = parser.add_argument_group('options')

    hparams.add_argument('-N', '--city_num', type=int, default=50, help="Number of task points in each sample")
    hparams.add_argument('-k', '--num_clusters', type=int, default=3, help="Number of clusters")
    hparams.add_argument('-F', '--feature_dim', type=int, default=2, help="Dimension of task point feature")
    hparams.add_argument('--sample_num', type=int, default=1000000, help="Sample number within the generated dataset")
    hparams.add_argument('-M', '--batch_size', type=int, default=32, help="Batch size to divide the dataset")
    hparams.add_argument('--lamb', type=float, default=0.5,
                         help="Lambda for balancing the distance cost and unsupervised losses")
    hparams.add_argument('--lamb_decay', type=float, default=1.0, help="Decay rate of lambda after each iteration")
    hparams.add_argument('--max_grad_norm', type=float, default=10.0, help="Threshold for gradient clipping")
    hparams.add_argument('--lr', '--learning_rate', type=float, default=0.01, help="Learning rate for the optimiser")
    hparams.add_argument('--embedding_dim', type=int, default=128,
                         help="Dimension of the embedder of the attention model")
    hparams.add_argument('--hidden_dim', type=int, default=128, help="Dimension of the hidden layer in MLP or MoE MLP")
    hparams.add_argument('--n_component', type=int, default=3, help="Number of experts for MoE")
    hparams.add_argument('--cost_d_op', choices=['sum', 'max'], type=str, default='sum',
                         help="Number of experts for MoE")

    options.add_argument('--model_type', type=str, choices=['mlp', 'moe_mlp', 'attention'], default='moe_mlp',
                         help="Type of the reinforcement agent model")
    options.add_argument('--data_type', type=str, choices=['blob', 'random'], default='random',
                         help="Type of generated dataset")
    options.add_argument('--log_dir', type=str, default='logs', help="Directory to save the logs")
    options.add_argument('--checkpoint_interval', type=int, default=200,
                         help="Interval to generate showcase and save model")
    options.add_argument('--gradient_check_flag', type=bool, default=False,
                         help="Whether to check the gradient flow")
    options.add_argument('--save_model', type=bool, default=True,
                         help="Whether to save the trained model")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = arg_parse()
    args
