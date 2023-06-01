# ECAPA-TDNN-Octuplet-Loss
Start from building the environment

```
conda create -n ECAPA python=3.7.9 anaconda
conda activate ECAPA
pip install -r requirements.txt
```

Start from the existing environment

```
pip install -r requirements.txt
```

### Training

Then you can change the data path in the `trainECAPAModel.py`. Train ECAPA-TDNN model end-to-end by using:

```
python trainECAPAModel.py --save_path exps/exp1 
```

### Pretrained model

```
python trainECAPAModel.py --eval --initial_model exps/pretrain.model
```

***


### Reference

Original ECAPA-TDNN paper

```
@inproceedings{desplanques2020ecapa,
  title={{ECAPA-TDNN: Emphasized Channel Attention, propagation and aggregation in TDNN based speaker verification}},
  author={Desplanques, Brecht and Thienpondt, Jenthe and Demuynck, Kris},
  booktitle={Interspeech 2020},
  pages={3830--3834},
  year={2020}
}
```

Our reimplement report

```
@article{das2021hlt,
  title={HLT-NUS SUBMISSION FOR 2020 NIST Conversational Telephone Speech SRE},
  author={Das, Rohan Kumar and Tao, Ruijie and Li, Haizhou},
  journal={arXiv preprint arXiv:2111.06671},
  year={2021}
}
```

VoxCeleb_trainer paper

```
@inproceedings{chung2020in,
  title={In defence of metric learning for speaker recognition},
  author={Chung, Joon Son and Huh, Jaesung and Mun, Seongkyu and Lee, Minjae and Heo, Hee Soo and Choe, Soyeon and Ham, Chiheon and Jung, Sunghwan and Lee, Bong-Jin and Han, Icksang},
  booktitle={Interspeech},
  year={2020}
}
```

### 
