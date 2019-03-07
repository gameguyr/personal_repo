function  read_in, filepath
cd, '~/Dropbox/final_search'

fin_cat = mrdfits(filepath, 1)
fin_cat = fin_cat[uniq(fin_cat.objid)]
return, fin_cat
end