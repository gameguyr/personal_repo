PRO GIvsIZ_testing_1, fin_cat
cd, '~/Dropbox/final_search'
error='0.05,0.05,0.05,0.05,.05'
;fin_cat = mrdfits('fin_cat.fits', 1)
;fin_cat = fin_cat[uniq(fin_cat.objid)]

;Defining some constants
ho = 100. ;KM/S/MPc
c=3.e5    ;KM/S


u = fin_cat.modelmag_u-fin_cat.EXTINCTION_u
g = fin_cat.modelmag_g-fin_cat.EXTINCTION_g
r = fin_cat.modelmag_r-fin_cat.EXTINCTION_r 
i = fin_cat.modelmag_i-fin_cat.EXTINCTION_i
z = fin_cat.modelmag_z-fin_cat.EXTINCTION_z
;j = fin_cat.j_1apermag3
;k = fin_cat.kapermag3

stars = WHERE(fin_cat.type eq 6)
gals  = WHERE(fin_cat.type eq 3)

ra = fin_cat.ra*(180/3.14159)       ;IN DEGREES
dec = fin_cat.dec*(180/3.14159)     ;IN DEGREES
;assumed_red=''
;read, assumed_red, PROMPT='enetr redshift of group'
;assumed_red = fin_cat.ASSUME   ;for the lowz_indexed assumed z
;assumed_red = 0.003600
;assumed_dist = (c/ho)*assumed_red   ; MEGA PARSECS
objid = fin_cat.objid
;radius = assumed_dist*1e6*(fin_cat.PETROR50_R/206265)

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




xrange = [-.2, .6]
yrange = [.5, 3]

split=strsplit(error, ',', /EXTRACT)
FOR t=0,  N_ELEMENTS(split)-1 do begin
  split[t] = float(split[t])
ENDFOR  
print, 'Ok,  lemme calculate some things for you'

      ;DEFINING THE MASKS

      u_mag_err_cut = fin_cat.modelmagerr_u lt split[0]
      g_mag_err_cut = fin_cat.modelmagerr_g lt split[1]
      r_mag_err_cut = fin_cat.modelmagerr_r lt split[2]
      i_mag_err_cut = fin_cat.modelmagerr_i lt split[3]
      z_mag_err_cut = fin_cat.modelmagerr_z lt split[4]

mag_mask = (g_mag_err_cut AND u_mag_err_cut $
      AND i_mag_err_cut AND z_mag_err_cut)
    
    index = WHERE(mag_mask)        
    i3=WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 3))
    i4=WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 6))
;    i5=WHERE(select2a AND sdss_flags_mask AND mag_mask)
    
!p.multi = [0, 1, 1]
OPLOT, i[i3]-z[i3], u[i3]-g[i3], psym=3, xr=xrange, yr=yrange, color=150, xs=1, ys=1, $
    xtitle='I - Z', ytitle='U - G', title='Flag + Mag Mask'
OPLOT, i[i4]-z[i4], u[i4]-g[i4], psym=3, color=150
!p.multi = [0, 1, 1]

stop
END