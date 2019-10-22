#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 7.13*y
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

atom(<  0.93,   0.32,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.02,  -1.23,  -0.01>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #1 
atom(<  1.85,  -1.23,  -0.01>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #2 
atom(<  0.93,  -0.72,  -0.34>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #3 
atom(<  0.93,   2.19, -13.35>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  0.93,  -0.73, -13.35>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -1.00,   0.73, -12.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(< -1.00,  -2.19, -12.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  2.87,   0.73, -12.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(<  2.87,  -2.19, -12.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(<  0.93,   2.19, -10.90>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(<  0.93,  -0.73, -10.90>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -2.23,   2.19, -10.19>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(< -2.23,  -0.73, -10.19>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(< -0.29,   0.73,  -8.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -0.29,  -2.19,  -8.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(<  2.16,   0.73,  -8.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  2.16,  -2.19,  -8.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(< -2.23,   2.19,  -7.74>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -2.23,  -0.73,  -7.74>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(<  0.93,   2.19,  -7.04>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  0.93,  -0.73,  -7.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(< -1.00,   0.73,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(< -1.00,  -2.19,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  2.86,   0.73,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(<  2.86,  -2.19,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(<  0.93,   2.19,  -4.63>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(<  0.93,  -0.73,  -4.60>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -2.23,   2.19,  -3.84>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(< -2.23,  -0.73,  -3.83>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(< -0.26,   0.80,  -2.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -0.26,  -2.26,  -2.49>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(<  2.13,   0.80,  -2.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(<  2.13,  -2.26,  -2.49>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #33 
atom(< -2.23,   2.19,  -1.34>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #34 
atom(< -2.23,  -0.74,  -1.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #35 
atom(< -2.23,   2.19, -12.12>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -0.73, -12.12>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(<  0.93,   0.73, -12.12>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -2.19, -12.12>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(< -2.23,   0.73,  -8.96>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,  -2.19,  -8.96>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(<  0.93,   2.19,  -8.96>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,  -0.73,  -8.96>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(< -2.23,   2.19,  -5.77>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,  -0.73,  -5.75>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(<  0.93,   0.70,  -5.85>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,  -2.16,  -5.85>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(< -2.23,   0.73,  -2.49>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #48 
atom(< -2.23,  -2.19,  -2.49>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #49 
atom(<  0.93,   2.19,  -2.83>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #50 
atom(<  0.93,  -0.73,  -2.39>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #51 
cylinder {<  0.93,  -0.72,  -0.34>, <  0.93,  -0.20,  -0.17>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.32,   0.00>, <  0.93,  -0.20,  -0.17>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.72,  -0.34>, <  0.48,  -0.98,  -0.18>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.02,  -1.23,  -0.01>, <  0.48,  -0.98,  -0.18>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.72,  -0.34>, <  1.39,  -0.98,  -0.18>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.85,  -1.23,  -0.01>, <  1.39,  -0.98,  -0.18>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -12.12>, < -1.62,   1.46, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.12>, < -1.62,   1.46, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -12.12>, < -2.23,   2.19, -11.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -10.19>, < -2.23,   2.19, -11.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.12>, < -1.62,   0.00, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.12>, < -1.62,   0.00, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.12>, < -1.62,  -1.46, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -12.12>, < -1.62,  -1.46, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.12>, < -2.23,  -0.73, -11.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.19>, < -2.23,  -0.73, -11.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, <  0.93,   1.46, -12.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -13.35>, <  0.93,   1.46, -12.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, <  0.93,   0.00, -12.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -13.35>, <  0.93,   0.00, -12.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, < -0.04,   0.73, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.12>, < -0.04,   0.73, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, <  1.90,   0.73, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,   0.73, -12.12>, <  1.90,   0.73, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, <  0.93,   1.46, -11.51>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -10.90>, <  0.93,   1.46, -11.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.12>, <  0.93,   0.00, -11.51>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.90>, <  0.93,   0.00, -11.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.12>, <  0.93,  -1.46, -12.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -13.35>, <  0.93,  -1.46, -12.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.12>, < -0.04,  -2.19, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -12.12>, < -0.04,  -2.19, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.12>, <  1.90,  -2.19, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -2.19, -12.12>, <  1.90,  -2.19, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.12>, <  0.93,  -1.46, -11.51>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.90>, <  0.93,  -1.46, -11.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.96>, < -2.23,   1.46,  -9.58>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -10.19>, < -2.23,   1.46,  -9.58>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.96>, < -2.23,   0.00,  -9.58>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.19>, < -2.23,   0.00,  -9.58>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.96>, < -1.26,   0.73,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.96>, < -1.26,   0.73,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.96>, < -2.23,   1.46,  -8.35>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -7.74>, < -2.23,   1.46,  -8.35>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.96>, < -2.23,   0.00,  -8.35>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.74>, < -2.23,   0.00,  -8.35>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.96>, < -2.23,  -1.46,  -9.58>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.19>, < -2.23,  -1.46,  -9.58>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.96>, < -1.26,  -2.19,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -8.96>, < -1.26,  -2.19,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.96>, < -2.23,  -1.46,  -8.35>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.74>, < -2.23,  -1.46,  -8.35>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.96>, <  0.93,   2.19,  -9.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -10.90>, <  0.93,   2.19,  -9.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.96>, <  0.32,   1.46,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.96>, <  0.32,   1.46,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.96>, <  1.54,   1.46,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -8.96>, <  1.54,   1.46,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.96>, <  0.93,   2.19,  -8.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.04>, <  0.93,   2.19,  -8.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  0.93,  -0.73,  -9.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.90>, <  0.93,  -0.73,  -9.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  0.32,   0.00,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.96>, <  0.32,   0.00,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  0.32,  -1.46,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -8.96>, <  0.32,  -1.46,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  1.54,   0.00,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -8.96>, <  1.54,   0.00,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  1.54,  -1.46,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.19,  -8.96>, <  1.54,  -1.46,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.96>, <  0.93,  -0.73,  -8.02>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.07>, <  0.93,  -0.73,  -8.02>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -5.77>, < -2.23,   2.19,  -6.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -7.74>, < -2.23,   2.19,  -6.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -5.77>, < -1.61,   1.46,  -5.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.81>, < -1.61,   1.46,  -5.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -5.77>, < -2.23,   2.19,  -4.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -3.84>, < -2.23,   2.19,  -4.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.75>, < -2.23,  -0.73,  -6.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.74>, < -2.23,  -0.73,  -6.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.75>, < -1.61,   0.00,  -5.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.81>, < -1.61,   0.00,  -5.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.75>, < -1.61,  -1.46,  -5.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19,  -5.81>, < -1.61,  -1.46,  -5.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.75>, < -2.23,  -0.73,  -4.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -3.83>, < -2.23,  -0.73,  -4.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, <  0.93,   1.45,  -6.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.04>, <  0.93,   1.45,  -6.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, <  0.93,  -0.01,  -6.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.07>, <  0.93,  -0.01,  -6.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, < -0.03,   0.72,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.81>, < -0.03,   0.72,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, <  1.89,   0.72,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   0.73,  -5.81>, <  1.89,   0.72,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, <  0.93,   1.45,  -5.24>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -4.63>, <  0.93,   1.45,  -5.24>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.85>, <  0.93,  -0.01,  -5.22>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.60>, <  0.93,  -0.01,  -5.22>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.85>, <  0.93,  -1.45,  -6.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.07>, <  0.93,  -1.45,  -6.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.85>, < -0.03,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19,  -5.81>, < -0.03,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.85>, <  1.89,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,  -2.19,  -5.81>, <  1.89,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.85>, <  0.93,  -1.45,  -5.22>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.60>, <  0.93,  -1.45,  -5.22>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -2.49>, < -2.23,   1.46,  -3.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -3.84>, < -2.23,   1.46,  -3.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -2.49>, < -2.23,  -0.00,  -3.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -3.83>, < -2.23,  -0.00,  -3.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -2.49>, < -1.24,   0.76,  -2.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.48>, < -1.24,   0.76,  -2.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -2.49>, < -2.23,   1.46,  -1.91>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -1.34>, < -2.23,   1.46,  -1.91>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -2.49>, < -2.23,  -0.00,  -1.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.74,  -1.36>, < -2.23,  -0.00,  -1.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -2.49>, < -2.23,  -1.46,  -3.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -3.83>, < -2.23,  -1.46,  -3.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -2.49>, < -1.25,  -2.23,  -2.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.26,  -2.49>, < -1.25,  -2.23,  -2.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -2.49>, < -2.23,  -1.47,  -1.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.74,  -1.36>, < -2.23,  -1.47,  -1.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -2.83>, <  0.93,   2.19,  -3.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -4.63>, <  0.93,   2.19,  -3.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -2.83>, <  0.33,   1.49,  -2.66>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.48>, <  0.33,   1.49,  -2.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -2.83>, <  1.53,   1.49,  -2.66>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,   0.80,  -2.48>, <  1.53,   1.49,  -2.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  0.93,  -0.73,  -1.37>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.72,  -0.34>, <  0.93,  -0.73,  -1.37>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  0.93,  -0.73,  -3.49>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.60>, <  0.93,  -0.73,  -3.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  0.34,   0.03,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.48>, <  0.34,   0.03,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  0.34,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.26,  -2.49>, <  0.34,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  1.53,   0.03,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,   0.80,  -2.48>, <  1.53,   0.03,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -2.39>, <  1.53,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,  -2.26,  -2.49>, <  1.53,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
