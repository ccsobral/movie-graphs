 #!/usr/bin/env bash

echo 'Setting up moviegraphs.db'

mkdir -p ./data

echo 'Downloading tar files from IMDB'
python downloads.py
echo 'Successfully downloaded tar files from IMDB'

#Extract only lines relating to films or TV shows from the tar
#Ignoring some columns we don't care about now
zcat ./data/basics.tsv.gz |\
    grep -E "(tconst|tvSeries|movie)" |\
    awk '{FS="\t"; OFS="\t"; if (NR!=1) $1=substr($1,3); print $1,$2,$3,$6,$7,$8,$9}' \
    > ./data/basics.tsv
echo 'Edited basics.tsv'

zcat ./data/episode.tsv.gz |\
    awk '{FS="\t"; OFS="\t"; if (NR!=1) {$1=substr($1,3); $2=substr($2,3);} print $0}' \
    > ./data/episodes.tsv
echo 'Edited episodes.tsv'

zcat ./data/ratings.tsv.gz |\
    awk '{FS="\t"; OFS="\t"; if (NR!=1) {$1=substr($1,3);} print $0}' \
    > ./data/ratings.tsv
echo 'Edited ratings.tsv'

echo 'Creating sqlite database...'
python create_sqlitedb.py
echo 'Successfully set up moviegraphs.db'
