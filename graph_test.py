import paddle_quantum.utils
import paddle.tensor
import numpy as np

test_array_a = np.random.rand(10,10) + np.random.rand(10,10) * 1j
result_array = paddle_quantum.utils.plot_density_graph(test_array_a)

test_tensor_a = paddle.to_tensor(test_array_a)
result_tensor = paddle_quantum.utils.plot_density_graph(test_tensor_a)
