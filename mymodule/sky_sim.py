#! /usr/bin/env python 
""" Determine Andromeda location in ra/dec degrees
"""

# convert to decimal degrees
from math import cos, pi
from random import uniform

NSRC = 1_000_000

# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

def clip_to_radius(ras, decs, ref_ra, ref_dec, radius):
    """
    Crop an input list of positions so that they lie within radius of
    a reference position

    Parameters
    ----------
    ras,decs : list(float)
        The ra and dec in degrees of the data points
    ref_ra, ref_dec: float
        The reference location
    radius: float
        The radius in degrees
    Returns
    -------
    ras, decs : list
        A list of ra and dec coordinates that pass our filter.
    """
    ra_out = []
    dec_out = []
    for i in range(len(ras)):
        if (ras[i]-ref_ra)**2 + (decs[i]-ref_dec)**2 < radius**2:
            ra_out.append(ras[i])
            dec_out.append(ras[i])
    return ra_out, dec_out

def generate_sky_pos():

    # Should do this with astropy
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)

    # make 1000 stars within 1 degree of Andromeda
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))

    return ras, decs, ra, dec

    

def main():
    ras, decs, ra, dec = generate_sky_pos()
    ras, decs = clip_to_radius(ras,decs, ra, dec, 1)

    # now write these to a csv file for use by my other program
    with open('catalog.csv','w') as f:
        print("id,ra,dec", file=f)
        for i in range(len(ras)):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
