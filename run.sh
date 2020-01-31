rm -rf images_background images_evaluation images_validation && \
curl -LO https://github.com/brendenlake/omniglot/raw/master/python/images_background.zip && \
curl -LO https://github.com/brendenlake/omniglot/raw/master/python/images_evaluation.zip && \
unzip images_background.zip && \
unzip images_evaluation.zip && \
mkdir images_validation && \
mv "images_background/Blackfoot_(Canadian_Aboriginal_Syllabics)" images_validation && \
mv "images_background/Ojibwe_(Canadian_Aboriginal_Syllabics)" images_validation && \
mv "images_background/Inuktitut_(Canadian_Aboriginal_Syllabics)" images_validation && \
mv "images_background/Tagalog" images_validation && \
mv "images_background/Alphabet_of_the_Magi" images_validation && \
python to_numpy.py && \
sha256sum images_background.npz > images_background.npz.sha256 && \
sha256sum images_validation.npz > images_validation.npz.sha256 && \
sha256sum images_evaluation.npz > images_evaluation.npz.sha256
