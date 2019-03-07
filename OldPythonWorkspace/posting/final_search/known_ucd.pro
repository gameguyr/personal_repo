pro known_ucd

hst=read_in('~/idlworkspace/default/lowz_project/hst_candidates.fits')
vcd=read_in('~/Dropbox/final_search/virgo_ucds.fits')
device, decompose=0
u = vcd.modelmag_u-vcd.EXTINCTION_u
g = vcd.modelmag_g-vcd.EXTINCTION_g
r = vcd.modelmag_r-vcd.EXTINCTION_r 
i = vcd.modelmag_i-vcd.EXTINCTION_i
z = vcd.modelmag_z-vcd.EXTINCTION_z

u1 = hst.modelmag_u-hst.EXTINCTION_u
g1 = hst.modelmag_g-hst.EXTINCTION_g
r1 = hst.modelmag_r-hst.EXTINCTION_r 
i1 = hst.modelmag_i-hst.EXTINCTION_i
z1 = hst.modelmag_z-hst.EXTINCTION_z
known_objid = [vcd.objid, hst.objid]

ra = vcd.ra*(180/3.14159)       ;IN DEGREES
dec = vcd.dec*(180/3.14159) 
ra1 = hst.ra*(180/3.14159)       ;IN DEGREES
dec1 = hst.dec*(180/3.14159) 
ra=[ra, ra1]
dec=[dec, dec1]
;u=[u, u1]
;g=[g, r1]
;r=[r, i1]
;i=[i, z1]
;z=[z, u1]





;;PLOTTING


loadct, 13
color_vcd=111
color_hst=220
oplot, i-z, u-g, psym=4, color=color_vcd, symsize=2
oplot, i1-z1, u1-g1, psym=4, color=color_hst, symsize=2
PLOTS, -.01, 2.3,  psym=4, color=color_hst, symsize=2
PLOTS, -.01,2.5,  psym=4, color=color_vcd, symsize=2

XYOUTS, [0, 0], [2.3, 2.5], ['HST UCDs','Virgo UCDs']
save, known_objid, filename='~/Dropbox/final_search/known_objid.sav'
forprint, ra, dec, textout='known_ra_dec.txt', NOCOMMENT=NO_COMMENT
stop
end