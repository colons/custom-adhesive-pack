"""
A utility script for downloading every character render from the Smash Bros.
website, including alternative colour palettes (where available).
"""

import subprocess

URL_FMT = 'https://www.smashbros.com/assets_v2/img/fighter/{}/main{}.png'
SLUGS = """
mario
donkey_kong
link
samus
dark_samus
yoshi
kirby
fox
pikachu
luigi
ness
captain_falcon
jigglypuff
peach
daisy
bowser
ice_climbers
sheik
zelda
dr_mario
pichu
falco
marth
lucina
young_link
ganondorf
mewtwo
roy
chrom
mr_game_and_watch
meta_knight
pit
dark_pit
zero_suit_samus
wario
snake
ike
pokemon_trainer
diddy_kong
lucas
sonic
king_dedede
olimar
lucario
rob
toon_link
wolf
villager
mega_man
wii_fit_trainer
rosalina_and_luma
little_mac
greninja
mii_fighter
palutena
pac_man
robin
shulk
bowser_jr
duck_hunt
ryu
ken
cloud
corrin
bayonetta
inkling
ridley
simon
richter
king_k_rool
isabelle
incineroar
piranha_plant
joker
dq_hero
banjo_and_kazooie
terry
byleth
minmin
steve
"""

if __name__ == '__main__':
    for fi, slug in enumerate((
        slug.strip() for slug in SLUGS.split('\n') if slug.strip()
    )):
        r = {
            'mii_fighter': range(1, 2),
        }

        for i in r.get(slug, range(1, 9)):
            url = URL_FMT.format(slug, i if i != 1 else '')
            subprocess.check_call([
                'wget', '--continue', url, '--output-document={}'.format(
                    f'{fi:02} {slug} {i}.png'
                )
            ])
