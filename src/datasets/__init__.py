from .mnist import MNIST, FashionMNIST
from .cifar import CIFAR10, CIFAR100
from .svhn import SVHN
from .tinyimagenet import TinyImageNet
from .imagenet import ImageNet
from .utils import *

__all__ = ('MNIST', 'FashionMNIST', 'CIFAR10', 'CIFAR100', 'SVHN', 'TinyImageNet', 'ImageNet')
