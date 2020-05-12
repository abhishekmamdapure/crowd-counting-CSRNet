# crowd-counting-CERNet

Check out some snapshots of the project that is implemented. 

<img src="Annotation 2020-05-12 222558.jpg" alt="Snap-shot-first-page" style="float: left; margin-right: 10px;" />
<img src="Annotation 2020-05-12 222710.jpg" alt="Snap-shot-first-page" style="float: right; margin-right: 10px;" />

> This project aims to estimate the count of the crowd using CSRNet model. 

- you can download the Shanghai dataset [here](https://www.kaggle.com/tthien/shanghaitech)
- get the repository to your local machine 

```git
git clone https://github.com/abhishekmamdapure/crowd-counting-CERNet.git
```
- download the pre-trained weights of the model from [here](https://www.dropbox.com/sh/b9aopkjxty84dhe/AACxP7SDjzc8Q9cXfsyBmgrya?dl=0)
- mention the downloaded  ``` 0model_best.pth.tar ``` in the project folder.
- open terminal  
>  ``` $  python app.py ```
- you will see the following o/p which means the code is running fine. 

 ```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 159-222-790
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

- head to your browser and enter address as ```  http://127.0.0.1:5000/ ``` and you will see the page as shown in the snapshot. 



### References 
- [Research Paper](https://arxiv.org/pdf/1802.10062.pdf)
- [Medium Article by Charlie Mackie](https://towardsdatascience.com/deploy-a-crowd-size-estimator-with-pytorch-size-ai-580903a101a5)

