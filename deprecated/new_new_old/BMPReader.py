from PIL import Image

from deprecated.new_new_old.Dormitory import Dormitory
from Enumeration import *
from deprecated.new_new_old.PartyZone import PartyZone
from deprecated.new_new_old.RoadTile import RoadTile
from deprecated.new_new_old.CampusBuilding import CampusBuilding


def get_map_as_dict():
    im = Image.open("bitmap.bmp")
    agh_map = {}
    roads = {}
    campus_buildings = {}
    party_zones = {}
    dormitories = {}
    for i in range(220):
        for j in range(69):
            r = im.getpixel((i, j))[0]
            g = im.getpixel((i, j))[1]
            b = im.getpixel((i, j))[2]
            to_write = None
            if r == 0:
                if g == 0:
                    if b == 0:
                        roads[i, j] = RoadTile()
                        to_write = TileType.Road
                    if b == 255:
                        campus_buildings[i, j] = CampusBuilding()
                        to_write = TileType.CampusBuilding
                if g == 255:
                    party_zones[i, j] = PartyZone()
                    to_write = TileType.PartyZone
            if r == 255:
                if g == 0:
                    if b == 0:
                        dormitories[i, j] = Dormitory()
                        to_write = TileType.Dormitory
            if to_write is not None:
                agh_map[i, j] = to_write
    return agh_map, roads, campus_buildings, party_zones, dormitories
    # print(mapped)
    # print(len(mapped))
    # print(im.format, im.size, im.mode, im.getcolors())
    # im.show()
