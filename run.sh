curl -LO https://github.com/brendenlake/omniglot/raw/master/python/images_background.zip
curl -LO https://github.com/brendenlake/omniglot/raw/master/python/images_evaluation.zip
unzip images_background.zip
unzip images_evaluation.zip
python to_numpy.py
sha256sum images_background.npz > images_background.npz.sha256
sha256sum images_evaluation.npz > images_evaluation.npz.sha256
