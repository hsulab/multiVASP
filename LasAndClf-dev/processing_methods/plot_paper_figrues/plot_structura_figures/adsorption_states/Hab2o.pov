#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 7.20*y
  direction 50.00*z
  location <0,0,50.00> look_at <0,0,0>}
light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}

#declare simple = finish {phong 0.7}
#declare pale = finish {ambient .5 diffuse .85 roughness .001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.10 roughness 0.04 }
#declare vmd = finish {ambient .0 diffuse .65 phong 0.1 phong_size 40. specular 0.500 }
#declare jmol = finish {ambient .2 diffuse .6 specular 1 roughness .001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.70 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient .15 brilliance 2 diffuse .6 metallic specular 1. roughness .001 reflection .0}
#declare glass = finish {ambient .05 diffuse .3 specular 1. roughness .001}
#declare glass2 = finish {ambient .0 diffuse .3 specular 1. reflection .25 roughness .001}
#declare Rcell = 0.100;
#declare Rbond = 0.200;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      translate LOC}
#end

atom(< -2.23,  -0.69,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.93,   2.23, -12.97>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(<  0.93,  -0.69, -12.97>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,   0.77, -11.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(< -1.00,  -2.15, -11.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,   0.77, -11.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  2.87,  -2.15, -11.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,   2.23, -10.52>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  0.93,  -0.69, -10.52>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,   2.23,  -9.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -2.23,  -0.69,  -9.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,   0.77,  -8.59>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -0.29,  -2.15,  -8.59>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,   0.77,  -8.59>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(<  2.16,  -2.15,  -8.59>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,   2.23,  -7.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(< -2.23,  -0.69,  -7.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,   2.23,  -6.66>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(<  0.93,  -0.69,  -6.65>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -1.00,   0.76,  -5.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(< -1.00,  -2.15,  -5.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.86,   0.76,  -5.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  2.86,  -2.15,  -5.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.93,   2.23,  -4.24>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  0.93,  -0.69,  -4.21>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.23,   2.23,  -3.52>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -2.23,  -0.69,  -3.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.30,   0.86,  -2.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -0.30,  -2.25,  -2.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.16,   0.86,  -2.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(<  2.16,  -2.25,  -2.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.23,   2.23,  -0.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.23,  -0.69,  -0.97>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(< -2.23,   2.23, -11.75>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(< -2.23,  -0.69, -11.75>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,   0.77, -11.75>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(<  0.93,  -2.15, -11.75>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,   0.77,  -8.59>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(< -2.23,  -2.15,  -8.59>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,   2.23,  -8.59>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(<  0.93,  -0.69,  -8.59>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,   2.23,  -5.42>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(< -2.23,  -0.69,  -5.37>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,   0.77,  -5.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(<  0.93,  -2.15,  -5.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,   0.85,  -2.17>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(< -2.23,  -2.23,  -2.17>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,   2.23,  -2.40>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(<  0.93,  -0.69,  -2.26>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #48 
cylinder {< -2.23,  -0.69,  -0.97>, < -2.23,  -0.69,  -0.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,   0.00>, < -2.23,  -0.69,  -0.49>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23, -11.75>, < -1.62,   1.50, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.75>, < -1.62,   1.50, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23, -11.75>, < -2.23,   2.23, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -9.81>, < -2.23,   2.23, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.75>, < -1.62,   0.04, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.75>, < -1.62,   0.04, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.75>, < -1.62,  -1.42, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15, -11.75>, < -1.62,  -1.42, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.75>, < -2.23,  -0.69, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.81>, < -2.23,  -0.69, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, <  0.93,   1.50, -12.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -12.97>, <  0.93,   1.50, -12.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, <  0.93,   0.04, -12.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -12.97>, <  0.93,   0.04, -12.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, < -0.04,   0.77, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.75>, < -0.04,   0.77, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, <  1.90,   0.77, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,   0.77, -11.75>, <  1.90,   0.77, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, <  0.93,   1.50, -11.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -10.52>, <  0.93,   1.50, -11.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.75>, <  0.93,   0.04, -11.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.52>, <  0.93,   0.04, -11.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15, -11.75>, <  0.93,  -1.42, -12.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -12.97>, <  0.93,  -1.42, -12.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15, -11.75>, < -0.04,  -2.15, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15, -11.75>, < -0.04,  -2.15, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15, -11.75>, <  1.90,  -2.15, -11.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -2.15, -11.75>, <  1.90,  -2.15, -11.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15, -11.75>, <  0.93,  -1.42, -11.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.52>, <  0.93,  -1.42, -11.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.59>, < -2.23,   1.50,  -9.20>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -9.81>, < -2.23,   1.50,  -9.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.59>, < -2.23,   0.04,  -9.20>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.81>, < -2.23,   0.04,  -9.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.59>, < -1.26,   0.77,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.59>, < -1.26,   0.77,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.59>, < -2.23,   1.50,  -7.97>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -7.36>, < -2.23,   1.50,  -7.97>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.59>, < -2.23,   0.04,  -7.97>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.36>, < -2.23,   0.04,  -7.97>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.15,  -8.59>, < -2.23,  -1.42,  -9.20>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.81>, < -2.23,  -1.42,  -9.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.15,  -8.59>, < -1.26,  -2.15,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.15,  -8.59>, < -1.26,  -2.15,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.15,  -8.59>, < -2.23,  -1.42,  -7.97>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.36>, < -2.23,  -1.42,  -7.97>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.59>, <  0.93,   2.23,  -9.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -10.52>, <  0.93,   2.23,  -9.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.59>, <  0.32,   1.50,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.59>, <  0.32,   1.50,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.59>, <  1.54,   1.50,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.77,  -8.59>, <  1.54,   1.50,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.59>, <  0.93,   2.23,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -6.66>, <  0.93,   2.23,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  0.93,  -0.69,  -9.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.52>, <  0.93,  -0.69,  -9.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  0.32,   0.04,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.59>, <  0.32,   0.04,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  0.32,  -1.42,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.15,  -8.59>, <  0.32,  -1.42,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  1.54,   0.04,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.77,  -8.59>, <  1.54,   0.04,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  1.54,  -1.42,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.15,  -8.59>, <  1.54,  -1.42,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.59>, <  0.93,  -0.69,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.65>, <  0.93,  -0.69,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.42>, < -2.23,   2.23,  -6.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -7.36>, < -2.23,   2.23,  -6.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.42>, < -1.61,   1.50,  -5.42>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.41>, < -1.61,   1.50,  -5.42>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.42>, < -2.23,   2.23,  -4.47>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -3.52>, < -2.23,   2.23,  -4.47>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.37>, < -2.23,  -0.69,  -6.37>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.36>, < -2.23,  -0.69,  -6.37>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.37>, < -1.61,   0.04,  -5.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.41>, < -1.61,   0.04,  -5.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.37>, < -1.61,  -1.42,  -5.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15,  -5.41>, < -1.61,  -1.42,  -5.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.37>, < -2.23,  -0.69,  -4.37>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -3.38>, < -2.23,  -0.69,  -4.37>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, <  0.93,   1.50,  -6.06>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -6.66>, <  0.93,   1.50,  -6.06>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, <  0.93,   0.04,  -6.06>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.65>, <  0.93,   0.04,  -6.06>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, < -0.03,   0.76,  -5.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.41>, < -0.03,   0.76,  -5.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, <  1.90,   0.76,  -5.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   0.76,  -5.41>, <  1.90,   0.76,  -5.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, <  0.93,   1.50,  -4.85>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -4.24>, <  0.93,   1.50,  -4.85>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77,  -5.46>, <  0.93,   0.04,  -4.84>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -4.21>, <  0.93,   0.04,  -4.84>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.46>, <  0.93,  -1.42,  -6.06>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.65>, <  0.93,  -1.42,  -6.06>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.46>, < -0.03,  -2.15,  -5.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15,  -5.41>, < -0.03,  -2.15,  -5.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.46>, <  1.90,  -2.15,  -5.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,  -2.15,  -5.41>, <  1.90,  -2.15,  -5.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.46>, <  0.93,  -1.42,  -4.84>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -4.21>, <  0.93,  -1.42,  -4.84>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.85,  -2.17>, < -2.23,   1.54,  -2.84>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -3.52>, < -2.23,   1.54,  -2.84>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.85,  -2.17>, < -2.23,   0.08,  -2.77>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -3.38>, < -2.23,   0.08,  -2.77>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.85,  -2.17>, < -1.26,   0.85,  -2.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   0.86,  -2.09>, < -1.26,   0.85,  -2.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.85,  -2.17>, < -2.23,   1.54,  -1.56>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -0.96>, < -2.23,   1.54,  -1.56>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.85,  -2.17>, < -2.23,   0.08,  -1.57>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -0.97>, < -2.23,   0.08,  -1.57>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.23,  -2.17>, < -2.23,  -1.46,  -2.77>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -3.38>, < -2.23,  -1.46,  -2.77>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.23,  -2.17>, < -1.26,  -2.24,  -2.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,  -2.25,  -2.09>, < -1.26,  -2.24,  -2.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.23,  -2.17>, < -2.23,  -1.46,  -1.57>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -0.97>, < -2.23,  -1.46,  -1.57>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -2.40>, <  0.93,   2.23,  -3.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -4.24>, <  0.93,   2.23,  -3.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -2.40>, <  0.32,   1.55,  -2.25>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   0.86,  -2.09>, <  0.32,   1.55,  -2.25>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -2.40>, <  1.55,   1.55,  -2.25>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.86,  -2.10>, <  1.55,   1.55,  -2.25>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -2.26>, <  0.93,  -0.69,  -3.24>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -4.21>, <  0.93,  -0.69,  -3.24>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -2.26>, <  0.32,   0.08,  -2.18>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   0.86,  -2.09>, <  0.32,   0.08,  -2.18>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -2.26>, <  0.32,  -1.47,  -2.18>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,  -2.25,  -2.09>, <  0.32,  -1.47,  -2.18>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -2.26>, <  1.55,   0.08,  -2.18>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.86,  -2.10>, <  1.55,   0.08,  -2.18>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -2.26>, <  1.55,  -1.47,  -2.18>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.25,  -2.09>, <  1.55,  -1.47,  -2.18>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
