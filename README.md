# hair-dye

<img src="./sample.png" width="576"/>

The architecture was proposed by [Alex L. Cheng C, etc. 'Real-time deep hair matting on mobile devices'](https://arxiv.org/pdf/1712.07168.pdf)

## Create environment

```
$ conda env create -f environment.yml
```

Activate environment

```
$ source activate hairdye
```

Deactivate the environment by

```
source deactivate
```

## Download dataset

```
$ sh download.sh
```

## Train

```
$ nohup python -u main.py --mode=train > out.log &
```

The checkpoint and sample images are saved in `src/checkpoint/default/` by default.

## Test
```
$ python main.py --mode=test
```

## Run

Plot a groundtruth image, the predicted segmentation and the hue adjusted result from the datasets or any specified image

```
$ python main.py --mode=run --set=test --num=4
$ python main.py --mode=run --image=./path/to/the/image.png
```

`set` can be one `train` and `test`, default is `test`

`num` is the random number of images from the set, default is `4`


## Convert the PyTorch model to Tensorflow model using ONNX

See the [notebook](./src/torch2tf.ipynb)

## Deploy the model to Android Application

See our other [repo](https://github.com/quq99/hair-dye-android)
#   H a i r - S e g m e n t a t i o n - b y - F i g a r o o - D a t a s e t  
 