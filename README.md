# python-study
this is the first project of mine

### Windows下安装python3

#### 下载链接

```
https://www.python.org/downloads/windows/
安装方式就一路点击下一步即可，会自动将python3添加到环境变量中
```

### Linux下安装python3

#### 下载链接

```
https://www.python.org/ftp/python/
```

#### 安装方式

1、下载对应版本的安装包，这次下载的是3.9.2版本，点击对应版本即可

![1638055467618](pictures/1638055467618.png)

2、在Linux下安装的话，选择这个Python-3.9.2.tgz，右键点击，复制下载链接

![1638055630581](pictures/1638055630581.png)

3、在Linux上执行

```
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
```

![1638060439334](pictures/1638060439334.png)

4、解压安装包

```
tar xvf Python-3.9.2.tgz
```



![1638061047112](pictures/1638061047112.png)

5、进入解压后的目录

```
cd Python-3.9.2
```

![1638061115317](pictures/1638061115317.png)

6、安装依赖包

```
yum -y install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

![1638061277302](pictures/1638061277302.png)

7、设置安装路径

```
 ./configure --prefix=/opt/python  --with-ssl
```

![1638061396437](pictures/1638061396437.png)

8、安装python3

```
make && make install
```

![1638061639227](pictures/1638061639227.png)

这样就是安装成功了

![1638063480640](pictures/1638063480640.png)

9、配置环境变量

```
ln -s /opt/python3/bin/python3 /usr/bin/python3
ln -s /opt/python3/bin/pip3 /usr/bin/pip3
```

![1638063623488](pictures/1638063623488.png)

10、修改pip安装源

```
vim ~/.pip/pip.conf
```

```conf
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
```

