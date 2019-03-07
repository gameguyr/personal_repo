PRO UG_IZ;, fin_cat, OP=op

cd, '~/Dropbox/final_search'
restore, 'known_objid.sav', /VERBOSE
error='0.13,0.05,0.05,0.05,.05'
fin_cat = mrdfits('fin_cat.fits', 1)
fin_cat = fin_cat[uniq(fin_cat.objid)]

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

ra = fin_cat.ra     ;IN DEGREES
dec = fin_cat.dec    ;IN DEGREES
;assumed_red=''
;read, assumed_red, PROMPT='enetr redshift of group'
;assumed_red = fin_cat.ASSUME   ;for the lowz_indexed assumed z
;assumed_red = 0.003600
;assumed_dist = (c/ho)*assumed_red   ; MEGA PARSECS
objid = fin_cat.objid
half_light_radius = fin_cat.PETROR50_R

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
sdss_mask1 = (fin_cat.flags AND (PEAKCENTER+NOTCHEKCED+DEBLEND_NOPEAK+BRIGHT $
+SATURATED+NOPROFILE)) eq 0 
sdss_mask2=(fin_cat.flags AND BINNED1) gt 0
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
           
;    i3 = WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 3) AND u-g GT 5*(i-z)+0.178 AND $
;         u-g LT 5*(i-z)+0.8 AND u-g GT 1.2 AND u-g LT 2.3 )
;  
;  
;    i4 = WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 6) AND u-g GT 5*(i-z)+0.178 AND $
;          u-g LT 5*(i-z)+0.8 AND u-g GT 1.2 AND u-g LT 2.3 )
;  
;  iall = WHERE(mag_mask AND sdss_flags_mask)
; 
;;  icut = WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 3) AND u-g GT 5*(i-z)+0.178 AND $
;;         u-g LT 5*(i-z)+0.8 AND u-g GT 1.2 AND u-g LT 2.3 AND u-g GT -(1D/13.5)*(i-z)+1.65 $
;;          AND u-g LT 13.5*(i-z)-1.65 AND fin_cat.PETROR50_R LT 0.8)
;          
;    icut = WHERE(mag_mask AND sdss_flags_mask AND u-g GT 5*(i-z)+0.178 AND $
;         u-g LT 5*(i-z)+0.8 AND u-g GT 1.2 AND u-g LT 2.3 AND u-g GT -(1D/13.5)*(i-z)+1.65 $
;          AND u-g LT 13.5*(i-z)-1.65 AND fin_cat.PETROR50_R LT 0.8)

    Flags = WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 3)
  
  
    i4 = WHERE(mag_mask AND sdss_flags_mask AND (fin_cat.TYPE eq 6)
          u-g LT 5*(i-z)+0.8 AND u-g GT 1.2 AND u-g LT 2.3 )
  
   iall = WHERE(mag_mask AND sdss_flags_mask)
 
          
    icut = WHERE(mag_mask AND sdss_flags_mask AND fin_cat.PETROR50_R LT 0.8)
 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Overplotting the new catalogs to see where they lie
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
IF keyword_set(OP) then begin
  OPLOT, i[iall]-z[iall], u[iall]-g[iall], psym=4, color=202;, symsize=3
endif else begin
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Plotting the Cut DAta
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;    
!p.multi = [0, 1, 1]
PLOT, i[i3]-z[i3], u[i3]-g[i3], psym=3, xr=xrange, yr=yrange, color=102, xs=1, ys=1, $
    xtitle='I - Z', ytitle='U - G', title='Flag + Mag Mask'
OPLOT, i[i4]-z[i4], u[i4]-g[i4], psym=3, color=170
;;criteria for the boxed regoin
OPLOT, i-z, 5*(i-z)+0.178 ;greater
OPLOT, i-z, 5*(i-z)+.8    ;less
OPLOT, i-z, -(1D/13.5)*(i-z)+1.65
OPLOT, i-z, 13.5*(i-z)-1.65

;OPLOT, i-z, 13.5*(i-z)-2.75 ;greater
;OPLOT, i-z, 9.5*(i-z)+0.13   ;less
!p.multi = [0, 1, 1]
endelse





forprint, ra[icut], dec[icut], textout='~/Dropbox/final_search/sample_ra_dec.txt', SILENT=1




stop
END