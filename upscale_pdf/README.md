# upscale_pdf
This Python Scripts uses ML Models to upscale scanned pdf to higher resolution pdf for crisp printing

## Model Used
Real ESRGAN model used. [Model](https://github.com/xinntao/Real-ESRGAN)
Model Tested in Google Colab Using Colab T4 GPU

Got to know about Real ESRGAN from [Upscayl](https://github.com/upscayl/upscayl). In Upscayl Digital_Art_4x they use Real ESRGAN model for upscaling digital art work. It produced Good Results.

Upscayl Changes Pytorch models (models.pt / models.pth) to light weigt C++ models in NCNN format. so that it can easily run on all low end devices/ Edge Devices. Optimised for CPU operations. 
Upscayl requires GPU for faster operation.

## Then why use Real ESRGAN model instead of directly using Upscayl.
Used Upscayl Digital_Art_4x model in windows desktop software [Link](https://upscayl.org/download), but it was taking so much time to process in low end laptop. Wanted to use Google Colab T4 GPU for faster Upscale.








