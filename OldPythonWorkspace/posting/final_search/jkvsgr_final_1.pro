PRO JKvsGR_final_1
cd, '~/Dropbox/final_search'
filePath= 'fin_cat.fits'
;read, filepath, PROMPT='Enter filepath'

;filename=strsplit(filepath, '.', /extract)
;filename=filename[0]
error='0.1,0.1,0.1,0.1'
fin_cat = mrdfits('fin_cat.fits', 1)
fin_cat = fin_cat[uniq(fin_cat.objid)]

;Defining some constants
ho = 100. ;KM/S/MPc
c=3.e5    ;KM/S



g = fin_cat.modelmag_g-fin_cat.EXTINCTION_g
r = fin_cat.modelmag_r-fin_cat.EXTINCTION_r 
j = fin_cat.j_1apermag3
k = fin_cat.kapermag3

ra = fin_cat.ra*(180/3.14159)       ;IN DEGREES
dec = fin_cat.dec*(180/3.14159)     ;IN DEGREES
;assumed_red=''
;read, assumed_red, PROMPT='enetr redshift of group'
assumed_red = fin_cat.ASSUME   ;for the lowz_indexed assumed z
;assumed_red = 0.003600
assumed_dist = (c/ho)*assumed_red   ; MEGA PARSECS
objid = fin_cat.objid
radius = assumed_dist*1e6*(fin_cat.PETROR50_R/206265)

; Defining color palette
device, decompose=0
loadct, 12

;Bitmasks

        ;SDSS FLAGS
PEAKCENTER='0000000000000020'x 
NOTCHEKCED='0000000000080000'x 
DEBLEND_NOPEAK='0000400000000000'x   
BRIGHT='0000000000000002'x   
SATURATED='0000000000040000'x   
NOPROFILE='0000000000000080'x
BINNED1='0000000010000000'x
sdss_mask1 = (fin_cat.flags_r AND (PEAKCENTER+NOTCHEKCED+DEBLEND_NOPEAK+BRIGHT $
+SATURATED+NOPROFILE)) eq 0 
sdss_mask2=(fin_cat.flags_r AND BINNED1) gt 0
sdss_mask3=fin_cat.primtarget eq 0
sdss_flags_mask= sdss_mask1 AND sdss_mask2

stars = WHERE(fin_cat.type eq 6)
gals  = WHERE(fin_cat.type eq 3)

        ;UKIDSS FLAGS
two=2ULL
BAD_PIXEL='00000040'x
CLOSE_TO_SATURATED='00010000'x
SOURCE_PER_FLATFIELD='00008000'x
SYSTEMATIC_ERROR='00080000'x
DITHER_OFFSET='00400000'x

ukidss_flags_mask = (fin_cat.J_1PPERRBITS AND (BAD_PIXEL+CLOSE_TO_SATURATED $
+ SOURCE_PER_FLATFIELD + SYSTEMATIC_ERROR +DITHER_OFFSET)) eq 0

;SIze Selection and Resolved cut
size_limit = 150. ;Parsecs
dPhot = 0.14
dSpec = 0.3
dR = ABS(fin_cat.psfmag_r - fin_cat.modelmag_r)

select1 = (dR gt 0.3 AND radius lt size_limit)
select2a = (dR gt dPhot AND dR lt dSpec)
select2b =  (dR lt dPhot)


x_roi = [0.55, 0.64,0.66, 1.1,  1.15,0.9,  0.55]
y_roi = [0.45, 0.73,0.87, 0.95, 0.75,0.45, 0.45]


check = 'yes'
check_2 ='yes'
str= ''
xrange = [0.6, 1.1]
yrange = [0.42, 0.95]

!p.MULTI = [0, 1, 2]

while check eq 'yes' do begin

    while check_2 eq 'yes' do begin

      split=strsplit(error, ',', /EXTRACT)
        FOR i=0,  N_ELEMENTS(split)-1 do begin
          split[i] = float(split[i])
        ENDFOR  
      print, 'Ok,  lemme calculate some things for you'

      ;DEFINING THE MASKS

      g_mag_err_cut = fin_cat.modelmagerr_g lt split[0]
      r_mag_err_cut = fin_cat.modelmagerr_r lt split[1]
      j_mag_err_cut = fin_cat.j_1apermag3err lt split[2]
      k_mag_err_cut =   fin_cat.kapermag3err lt split[3]

      mag_mask = (g_mag_err_cut AND r_mag_err_cut $
      AND j_mag_err_cut AND k_mag_err_cut)
    
    index = WHERE(mag_mask)        
    i3=WHERE(mag_mask AND sdss_flags_mask AND ukidss_flags_mask)
    i4=WHERE(select1 AND sdss_flags_mask AND ukidss_flags_mask AND mag_mask)
;TESTING    ;i4=WHERE(select2a AND sdss_flags_mask AND ukidss_flags_mask AND mag_mask)
    i5=WHERE(select2a AND sdss_flags_mask AND ukidss_flags_mask AND mag_mask)
    
    PLOT, j[i3]-k[i3], g[i3]-r[i3], psym=3, xr=xrange, yr=yrange, color=80, xs=1, ys=1, $
    xtitle='J - K', ytitle='G - R', title='Flag + Mag Mask'
         
    ;MAking the histogram for the R-BAND
    absMag_r   = r[i3]-5*ALOG10(assumed_dist[i3])-25
    mag_r_func = HISTOGRAM(absMag_r, BINSIZE=0.5 , LOC=r_bins, MIN=-24, MAX=0)
    PLOT, r_bins, mag_r_func, psym=10, color=40, xtitle='Assumed Absolute Magnitude in R-BAND', $
    ytitle='Number Of Objects';, yr=[0, 4e4]
    
    print, 'Do you want to Alter the error?  yes/no  '
    read, check_2
    
    if check_2 eq 'yes' then begin
          print, 'Please enter error in each band    '
          read, error
    endif
    
  endwhile

    
    PLOT, j[i4]-k[i4], g[i4]-r[i4], psym=5, xr=xrange, yr=yrange, color=80,$
    xs=1, ys=1,xtitle='J - K', ytitle='G - R', title='Poorly Resolved + Flags + mag Mask'
    
    PLOTs, x_roi,y_roi, color=40
     
    PLOT, j[i5]-k[i5], g[i5]-r[i5], psym=5, xr=xrange, yr=yrange , color=80,$
     xs=1, ys=1,xtitle='J - K', ytitle='G - R', title='Unresolved + Flags + mag Mask'
    
    PLOTs, x_roi,y_roi, color=40
    
    print, 'Do you want to Alter the error?  yes/no  '
    read, check_2
      
    print, 'Do you want to keep going?  yes/no  '
    read, check
    
endwhile
    !p.MULTI = 0
    
;Plotting into postscript once all the corrections have been made
set_plot, 'ps'
device, file='the_candidates.ps'

    PLOT, j[i4]-k[i4], g[i4]-r[i4], psym=5, xr=xrange, yr=yrange, color=80,$
    xs=1, ys=1,xtitle='J - K', ytitle='G - R', title='Poorly Resolved + Flags + mag Mask'
    
    PLOTs, x_roi,y_roi, color=40
     
    PLOT, j[i5]-k[i5], g[i5]-r[i5], psym=5, xr=xrange, yr=yrange, color=80,$
     xs=1, ys=1,xtitle='J - K', ytitle='G - R', title='Unresolved + Flags + mag Mask'
    
    PLOTs, x_roi,y_roi, color=40
device, /close
set_plot, 'x'


;Extracting the coordinates of the objects that fall within the ROI 
roi = obj_new('IDLanROI', x_roi, y_roi)
jk4=j[i4]-k[i4]
jk5=j[i5]-k[i5]
gr4=g[i4]-r[i4]
gr5=g[i5]-r[i5]
obj_id4 = objid[i4]
obj_id5 = objid[i5]

result4 = roi->ContainsPoints(jk4, gr4)
result5 = roi->ContainsPoints(jk5, gr5)

x4 = where(result4 eq 1)
x5 = where(result5 eq 1)

r4=ra[i4]
d4=dec[i4]

r5=ra[i5]
d5=dec[i5]

new_cat4 = fin_cat[i4]
new_cat5 = fin_cat[i5]

r4=r4[x4]
d4=d4[x4]

r5=r5[x5]
d5=d5[x5]

new_cat4 = new_cat4[x4]
new_cat5 = new_cat5[x5]


obj_id4 = obj_id4[x4]
obj_id5 = obj_id5[x5]
unique4 = uniq(obj_id4)
unique5 = uniq(obj_id5)
spawn, 'pwd', dir

mwrfits, new_cat4[unique4], 'candidate_4.fits',/create
mwrfits, new_cat5[unique5], 'candidate_5.fits',/create

forprint, r4[unique4],d4[unique4], $
textout=dir[0]+'/citeria_a.txt', /nocomment

forprint, r5[unique5],d5[unique5], $
textout=dir[0]+'/criteria_b.txt', /nocomment

print, 'There are    ', N_ELEMENTS(r4[unique4]), $
' objects with > dSpec and R <'+string(size_limit)


print, 'There are    ', N_ELEMENTS(r5[unique5]), $
' objects with dSpec > dObject > dPhot'

stop
END