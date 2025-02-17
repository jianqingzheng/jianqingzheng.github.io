<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>

<h1 id="-publications"><i class="fas fa-brain fa-spin"></i> Selected Research Projects<div style="float:right;"> [<a href="https://scholar.google.co.uk/citations?user=2bNsYR0AAAAJ"><i class="fas fa-graduation-cap"></i></a>] </div></h1>

## a. Biomedical Data Analysis

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">Preprint</div>
<img src='images/pubs/DRDM-graphic_abstract.png' alt="sym" width="100%" title="The graphic abstract of Deformation-Recovery Diffusion Model.">
<img src='images/pubs/drdm_demo.gif' loading="lazy" alt="sym" width="100%" title="An examplar DRDM result">
</div></div>
<div class='paper-box-text' markdown="1">
[Deformation-Recovery Diffusion Model (DRDM): Instance Deformation for Image Manipulation and Synthesis](https://jianqingzheng.github.io/def_diff_rec/)

<div class="inline-container">
<a href="https://jianqingzheng.github.io/def_diff_rec/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fjianqingzheng.github.io%2Fdef_diff_rec%2F&up_message=online&up_color=darkcyan&down_message=offline&down_color=darkgray&label=Project%20Page"></a>
<a href="https://doi.org/10.48550/arXiv.2407.07295"><img src="https://img.shields.io/badge/arXiv-2407.07295-b31b1b.svg" alt="arXiv"></a>
<a href="https://github.com/jianqingzheng/def_diff_rec"><img src="https://img.shields.io/github/stars/jianqingzheng/def_diff_rec?style=social&label=Code+★" alt="code"></a>
<a href="https://colab.research.google.com/github/jianqingzheng/def_diff_rec/blob/main/def_diff_rec.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
</div>

**J. Q. Zheng**<abbr title="equal contribution">†</abbr>, Y. Mo<abbr title="equal contribution">†</abbr>, Y. Sun, J. Li, F. Wu, Z. Wang, T. Vincent, B. W. Papiez

- This is the **first study** to explore diverse deformation generation for one specific image without an atlas image.

<div class="small-box">
<ul>
	<li>- A novel diffusion model is proposed based on deformation diffusion and recovery. </li>
	<li>- The model generates diverse and realistic deformation for each instance image. </li>
	<li>- A random and reasonable deformation field sampling method is proposed for training. </li>
	<li>- The model enables and improves data augmentation in few-shot segmentation.</li>
	<li>- The model enables and improves data synthesis for registration model training. </li>
</ul>
</div>
</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">Med Image Anal (IF:13.8)</div>
<img src='images/pubs/RAN-graphic_abstract.jpg' alt="sym" width="100%" title="The graphic abstract of Residual Aligner Network.">
<img src='images/pubs/deformable_reg.gif' loading="lazy" alt="sym" width="100%" title="An examplar deformable registration result">
</div></div>
<div class='paper-box-text' markdown="1">
[Residual Aligner-based Network (RAN): Motion-Separable Structure for Coarse-to-fine Discontinuous Deformable Registration](https://jianqingzheng.github.io/res_aligner_net/)

<div class="inline-container">
<a href="https://jianqingzheng.github.io/res_aligner_net/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fjianqingzheng.github.io%2Fres_aligner_net%2F&up_message=online&up_color=darkcyan&down_message=offline&down_color=darkgray&label=Project%20Page"></a>
<a href="https://doi.org/10.1016/j.media.2023.103038"><img src="https://img.shields.io/badge/DOI-10.1016%2Fj.media.2023.103038-darkyellow" alt="DOI"></a>
<a href="https://arxiv.org/abs/2203.04290"><img src="https://img.shields.io/badge/arXiv-2203.04290-b31b1b.svg" alt="arXiv"></a>
<a href="https://github.com/jianqingzheng/res_aligner_net"><img src="https://img.shields.io/github/stars/jianqingzheng/res_aligner_net?style=social&label=Code+★" alt="code"></a>
<a href="https://colab.research.google.com/github/jianqingzheng/res_aligner_net/blob/main/res_aligner_net.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
<div class="dropdown">
<button class="dropdown-button"><i class='fas fa-blog' style='color:white'></i> Related Blogs </button>
<div class="dropdown-content">
    <a href="https://blog.csdn.net/amusi1994/article/details/135903644">CSDN博客</a>
    <a href="https://mp.weixin.qq.com/s/QV_MiNLzZMpKNw1vy_0yXA">CVer公众号</a>
</div>
</div>
</div>

**J. Q. Zheng**, Z. Wang, B. Huang, N. H. Lim, B. W. Papiez

- This is the **first quantitative investigation** of deep learning methods for **discontinuous deformable registration**.

<div class="small-box">
<ul>
	<li>- The proposed RAN obtains the state-of-the-art accuracy and better efficiency. </li>
	<li>- Motion separability quantifies upper limit of the predictable motions' difference. </li>
	<li>- Motion-Separable structure is used for a higher motion separability. </li>
	<li>- Multi-head mask is used to disentangle the motions of different organs.</li>
	<li>- Confidence weight is estimated to the weight and refine the predicted motions. </li>
</ul>
</div>
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">CMIG (IF:7.4) + MICCAIW 2020</div>
<img src='images/pubs/dnet-graphic_abstract.jpg' alt="sym" width="100%" title="D-net can align two CT volume from arbitrary orientation.">
<img src='images/pubs/cartilage_area.jpg' alt="sym" width="100%" title="The subtraction between aligned CT scans with and without contrast enhancement highlights the cartilage area."></div></div>
<div class='paper-box-text' markdown="1">
[Accurate volume alignment of arbitrarily oriented tibiae based on a mutual attention network for osteoarthritis analysis](https://www.sciencedirect.com/science/article/pii/S0895611123000228)
\| 
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.compmedimag.2023.102204-darkyellow)](https://doi.org/10.1016/j.compmedimag.2023.102204)
[![Patent](https://img.shields.io/badge/Patent-pending-orange)]()

[D-net: siamese based network for arbitrarily oriented volume alignment](https://link.springer.com/chapter/10.1007/978-3-030-61056-2_6)
\| 
[![DOI](https://img.shields.io/badge/DOI-10.1007%2F978--3--030--61056--2__6-darkyellow)](https://doi.org/10.1007/978-3-030-61056-2_6)
[![arXiv](https://img.shields.io/badge/arXiv-2101.10248-b31b1b.svg)](https://arxiv.org/abs/2101.10248)

**J. Q. Zheng**, N. H. Lim, B. W. Papiez

- It is the **earliest work** that applies the **attention mechanism** to **image registration**, enabling **sub-voxel errors** even from an arbitrary initial orientation.

<div class="small-box">
<ul>
	<li>- Alignment of arbitrary oriented CT volumes allows extraction of contrasted cartilage.</li>
	<li>- Only proposed D-net achieved accurate alignment of arbitrary oriented volumes.</li>
	<li>- D-net extracts the common features and the spatial information via Siamese structure.</li>
	<li>- Mutual attention enhances long-range connection between two-branch D-net structure.</li>
	<li>- The alignment framework may be generalizable for multiple longitudinal studies.</li>
</ul>
</div>
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">ICRA 2020</div>
<img src='images/pubs/125.gif' loading="lazy" alt="sym" width="49%" title="The dilation setting (1,2,5...) in DeepLab results in a smaller receptive field even though with more layers.">
<img src='images/pubs/139.gif' loading="lazy" id="acnn_rf" alt="sym" width="49%" title="Our dilation setting (1,3,9...) in ACNN results in a larger receptive field with fewer layers."></div></div>
<div class='paper-box-text' markdown="1">
[ACNN: a Full Resolution DCNN for Medical Image Segmentation](https://doi.org/10.1109/ICRA40945.2020.9197328)

[![DOI](https://img.shields.io/badge/DOI-10.1109%2FICRA40945.2020.9197328-darkyellow)](https://doi.org/10.1109/ICRA40945.2020.9197328)
[![arXiv](https://img.shields.io/badge/arXiv-1901.09203-b31b1b.svg)](https://arxiv.org/abs/1901.09203)
[![](https://img.shields.io/github/stars/XiaoYunZhou27/ACNN?style=social&label=Code+★)](https://github.com/XiaoYunZhou27/ACNN)

X. Y. Zhou<abbr title="equal contribution">†</abbr>, **J. Q. Zheng**<abbr title="equal contribution">†</abbr>, P. Li, G. Z. Yang

- A **pooling-free network structure** is proposed to achieve **full-resolution** feature processing using a **theoretically optimal dilation setting** for a larger receptive field, which achieves a **higher accuracy** even with **fewer parameters**.

<div class="small-box">
<ul>
	<li>- The left figure shows the receptive field with the dilation setting (1,2,5...) used for DeepLab.</li>
	<li>- The right figure shows the receptive field with the dilation setting (1,3,9...) used for our ACNN.</li>
	<li>- Our setting achieves larger receptive field with the same number of layers.</li>
</ul>
</div>
</div>
</div>

## b. Surgical Navigation

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">ICRA 2019</div>
<img src='images/pubs/demo-recover.gif' loading="lazy" alt="sym" width="50%" title="The 3D abdominal aortic center line recovered from one 2D X-ray image.">
<img src='images/pubs/demo-visual.gif' loading="lazy" alt="sym" width="48%" title="How it looks like when a catheter moves along the recovered center line of aorta."></div></div>
<div class='paper-box-text' markdown="1">
[Towards 3D Path Planning from a Single 2D Fluoroscopic Image for Fenestrated Endovascular Aortic Repair](https://ieeexplore.ieee.org/abstract/document/8793918)

[![DOI](https://img.shields.io/badge/DOI-10.1109%2FICRA.2019.8793918-darkyellow)](https://ieeexplore.ieee.org/abstract/document/8793918/)
[![arXiv](https://img.shields.io/badge/arXiv-1809.05955-b31b1b.svg)](https://arxiv.org/abs/1809.05955)
[![code](https://img.shields.io/github/stars/jianqingzheng/path_planning_for_FEVAR?style=social&label=Code+★)](https://github.com/jianqingzheng/path_planning_for_FEVAR)

**J. Q. Zheng**, X. Y. Zhou, C. Riga, G. Z. Yang

- The first **real-time framework** of 3D intra-operative AAA skeleton instantiation from a single 2D AAA fluoroscopic image is proposed for **3D robotic path planning**, achieving **sub-pixel error** in the clinical data.

<div class="small-box">
<ul>
	<li> - Left: the 3D abdominal aortic center line recovered from one 2D X-ray image. </li>
	<li> - Right: how it looks like when a catheter moves along the recovered center line of aorta.</li>
</ul>
</div>
</div>
</div>

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">MICCAI 2022</div>
<img src='images/pubs/m3depth_framework.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Self-Supervised Depth Estimation in Laparoscopic Image using 3D Geometric Consistency](https://doi.org/10.1007/978-3-031-16449-1_2)

[![DOI](https://img.shields.io/badge/DOI-10.1007%2F978--3--031--16449--1__2-darkyellow)](https://doi.org/10.1007/978-3-031-16449-1_2)
[![arXiv](https://img.shields.io/badge/arXiv-2208.08407-b31b1b.svg)](https://arxiv.org/abs/2208.08407)
[![code](https://img.shields.io/github/stars/br0202/M3Depth?style=social&label=Technique Code+★)](https://github.com/br0202/M3Depth)
[![code](https://img.shields.io/github/stars/br0202/SL-Decoder?style=social&label=Data+★)](https://github.com/br0202/SL-Decoder)

B. Huang, **J. Q. Zheng**, A. Nguyen, C. Xu, I. Gkouzionis, K. Vyas, D. Tuch, S. Giannarou, D. S. Elson

<div class="small-box">
<ul>
	<li>- Most recent depth estimation work focused on the left-right consistency in 2D and ignored valuable inherent 3D information on the object in real world coordinates, meaning that the left-right 3D geometric structural consistency is not fully utilized. </li>
	<li>- To overcome this limitation, we present M3Depth, a self-supervised depth estimator to leverage 3D geometric structural information hidden in stereo pairs while keeping monocular inference. </li>
	<li>- The method also removes the influence of border regions unseen in at least one of the stereo images via masking, to enhance the correspondences between left and right images in overlapping areas. </li>
	<li>- Extensive experiments show that our method outperforms previous self-supervised approaches on both a public dataset and a newly acquired dataset by a large margin, indicating a good generalization across different samples and laparoscopes.</li>
</ul>
</div>

</div>
</div>

## c. Computational Biology and Bioinformatics

<div class='paper-box'>
<div class='paper-box-image'><div><div class="badge">Cell Research (IF:46.3)</div>
<img src='images/pubs/xbcrnet.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Deep learning-based rapid generation of broadly reactive antibodies against SARS-CoV-2 and its Omicron variant](https://www.nature.com/articles/s41422-022-00727-6)

<div class="inline-container">
<a href="https://jianqingzheng.github.io/XBCR-net/">
    <img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fjianqingzheng.github.io%2FXBCR-net%2F&up_message=online&up_color=darkcyan&down_message=offline&down_color=darkgray&label=Project%20Page">
</a>
<a href="https://www.nature.com/articles/s41422-022-00727-6"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs41422--022--00727--6-darkyellow" alt="DOI"></a>
<a href="https://github.com/jianqingzheng/XBCR-net"><img src="https://img.shields.io/github/stars/jianqingzheng/XBCR-net?style=social&label=Code+★" alt="GitHub stars"></a>
<a href="https://colab.research.google.com/github/jianqingzheng/XBCR-net/blob/main/XBCR_net.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Explore XBCR-net in Colab"></a>
<div class="dropdown">
<button class="dropdown-button"><i class='fas fa-blog' style='color:white'></i> Related Blogs </button>
<div class="dropdown-content">
    <a href="https://mp.weixin.qq.com/s/fDeRXs8Cq0L_LzYvZlI1iA">iNature公众号</a>
    <a href="https://www.jianshu.com/p/738566843214">简书</a>
</div>
</div>
<div class="dropdown">
<button class="dropdown-button" style="background-color: #3f003f"><i class='fas fa-globe' style='color:white'></i> Related News </button>
<div class="dropdown-content">
    <a href="https://eng.ox.ac.uk/case-studies/artificial-intelligence-and-big-data-help-rapid-screening-antibodies">eng.ox.ac.uk</a>
    <a href="https://en.nankai.edu.cn/2022/1115/c22796a495042/page.htm">news.nankai.edu</a>
    <a href="https://www.toutiao.com/article/7156887617291092480/?wid=1710118034547">今日头条</a>
    <a href="https://www.sohu.com/a/588753859_183834">搜狐网</a>
</div>
</div>
</div>

H. Lou<abbr title="equal contribution">†</abbr>, **J. Q. Zheng**<abbr title="equal contribution">†</abbr>, X. Fang, Z. Liang, M. Zhang, Y. Chen, C. Wang, and X. Cao. 

- The **first** deep learning method is proposed for predicting **cross-reactive antibodies**, using <a href="/#acnn_rf">ACNN</a> structure for feature extraction.

<div class="small-box">
<ul>
	<li>a. The features of the amino acid sequences of VH, VL and RBD sequences were extracted, localized and max-pooled to be concatenated together as input to the fully connected layers. 
	The active features in the latent space were then processed by Multi-Layer Perceptron to predict the binding probability of antibody to multiple antigens. 
	The impact score of VH, VL and RBD is calculated on the local histogram impact score map, representing how much weight is given to the specified amino acids on VH, VL (y axis) and RBD (x axis). 
	Prediction results are evaluated by Precision-Recall curves of ACNN (Violet), Transformer (Gray), FCN (Red) and CNN (Blue). 
	</li>
	<li>b. The HCDR3 sequences of the predicted SARS-CoV-2 and Omicron variant binders are clustered by using an 80% sequence similarity. 
	Cluster size represents the number of BCR sequences in the cluster. 
	For each expanded cluster, the HCDR3 sequences are visualized as a sequence logo plot, where y-axis represents the frequency of the individual amino acid at the corresponding position in x-axis. 
	The frequency of the dominating VH gene is listed above the logo. 
	</li>
	<li>c. Circos plot showing the frequency of antibodies encoded by the specified V region to J region pairing of the pan-SARS2 sequences. 
	</li>
	<li>d. The diversity of the four groups of BCR repertoire is analyzed, which is linked to the sample number of each group. 
	</li>	
	<li>e. Binding of the predicted cross-reactive antibodies to RBD of SARS-CoV-2 and Omicron variants (left panel) was examined by ELISA. 
	Representative OD reading is plotted as heatmap ranging from 0.05 to 5.0, and OD of 0.1 is used as cut-off value (n = 3 per group). 
	</li>
	<li>f. The SARS-CoV-2 Omicron variant (BA.1) pseudovirus neutralization curves of XBN-1, XBN-6 and XBN-11 mAbs were generated from luciferase readings at 8 dilutions (n = 3). 
	</li>
	<li>g. HCDR3 sequences of the XBN-1 and XBN-11 are aligned with the most convergent anti-SARS-CoV-2 antibodies from the published studies. 
	</li>
	<li>h. The HCDR3 sequence frequency of the dominant cluster (encoded by IGHV3-30 and IGKV1-13) of the pan-SARS group is shown.
	</li>
</ul>
</div>
</div>
</div>

