#!/Users/xander/.pyenv/shims/python

from time import time, sleep
from lib import bar_socket, bar_chat
import threading

USERNAME = ""
PASSWORD = ""

# Create a TCP/IP socket
sock = bar_socket.craft_socket()

# Connect the socket to the port where the server is listening
server_address = ('server3.beyondallreason.info', 8200)

bar_socket.connect_socket(sock, server_address)


def ping():
    ping_no = 1
    while True:
        ping_msg = "#%d PING" % ping_no
        print(ping_msg)
        bar_socket.send_message(sock, "%s\n" % ping_msg)
        ping_no += 1
        sleep(20)


ping_thread = threading.Thread(target=ping, args=())
ping_thread.start()


def create_battle():
    battle_id = ""
    login_info_ended = False

    while True:
        try:
            message = bar_socket.receive_message(sock)
        except:
            break

        print(message)

        if "TASSERVER" in message:
            bar_socket.send_message(
                sock, 'LOGIN %s %s 0 * LuaLobby Chobby	2741051649 a6187192662d168e	b sp\n' % (USERNAME, PASSWORD))
        elif "AGREEMENT" in message:
            bar_socket.send_message(
                sock, 'CONFIRMAGREEMENT\n')
        elif "LOGININFOEND" in message:
            login_info_ended = True
            bar_socket.send_message(
                sock, "OPENBATTLE 0 0 empty 52200 16 -1540855590 0 1565299817 spring\t105.1.1-1214-gcf8d087 BAR105\tauth_joinbattle_test\tEU - 00\tBeyond All Reason test-21140-5db4903\n")
        elif login_info_ended:
            if "BATTLEOPENED" in message:
                battle_id = message.split(" ")[1]
                bar_socket.send_message(
                    sock, "UPDATEBATTLEINFO 1 0 1565299817 Comet Catcher Remake 1.8\n")
                bar_socket.send_message(sock, "SETSCRIPTTAGS game/modoptions/starttime=0	game/modoptions/captureradius=100	game/modoptions/multiplier_radarrange=1	game/modoptions/critters=1	game/modoptions/newdgun=0	game/modoptions/chicken_queenanger=1	game/modoptions/experimentalscavuniqueunits=0	game/modoptions/unit_restrictions_noconverters=0	game/modoptions/tweakunits8=	game/modoptions/tweakunits3=	game/modoptions/ruins_density=normal	game/modoptions/scoremode_chess_adduptime=4	game/modoptions/scavtechcurve=1	game/modoptions/commanderbuildersrange=1500	game/modoptions/tweakunits6=	game/modoptions/experimentalxpgain=1	game/modoptions/experimentalrebalancet2metalextractors=0	game/modoptions/tugofwarmodifier=1	game/modoptions/ruins_only_t1=0	game/modoptions/tweakunits7=	game/modoptions/experimentalrebalancewreckstandarization=1	game/modoptions/experimentalreversegear=0	game/modoptions/tweakdefs3=	game/modoptions/assistdronescount=4	game/modoptions/commanderbuildersenabled=pve_only	game/modoptions/map_atmosphere=1	game/modoptions/tweakdefs=	game/modoptions/scavunitspawnmultiplier=1	game/modoptions/resourceincomemultiplier=1	game/modoptions/unbatech=0	game/modoptions/coop=0	game/modoptions/decapspeed=2	game/modoptions/capturebonus=100	game/modoptions/scavunitcountmultiplier=1	game/modoptions/debugcommands=	game/modoptions/assistdronesenabled=pve_only	game/modoptions/allowuserwidgets=1	game/modoptions/scoremode_chess_unbalanced=0	game/modoptions/dominationscore=1000	game/modoptions/tweakdefs1=	game/modoptions/experimentalimprovedtransports=0	game/modoptions/tweakunits1=	game/modoptions/chicken_swarmmode=0	game/modoptions/ai_incomemultiplier=1	game/modoptions/experimentalnoaircollisions=0	game/modoptions/startmetal=1000	game/modoptions/disablemapdamage=0	game/modoptions/unit_restrictions_notech2=0	game/modoptions/tweakdefs6=	game/modoptions/disable_fogofwar=0	game/modoptions/experimentalrebalancet2energy=0	game/modoptions/chicken_difficulty=normal	game/modoptions/scavmaxtechlevel=tech4	game/modoptions/scavevents=1	game/modoptions/unit_restrictions_noair=0	game/modoptions/lootboxes_density=normal	game/modoptions/experimentalshieldpower=1	game/modoptions/multiplier_losrange=1	game/modoptions/metalperpoint=1	game/modoptions/ruins_civilian_disable=0	game/modoptions/experimentalmorphs=0	game/modoptions/tweakdefs4=	game/modoptions/fixedallies=1	game/modoptions/multiplier_maxvelocity=1	game/modoptions/unit_restrictions_nolrpc=0	game/modoptions/energyperpoint=75	game/modoptions/scavbosstoggle=1	server/match/uuid=33de8927-a3f5-47e7-926d-8464e7d9ca06	game/modoptions/scaveventsamount=normal	game/modoptions/chicken_spawncountmult=1	game/modoptions/scoremode_chess=1	game/modoptions/limitscore=300	game/modoptions/scavdifficulty=medium	game/modoptions/tweakdefs5=	game/modoptions/unba=0	game/modoptions/chicken_maxchicken=300	game/modoptions/startenergy=1000	game/modoptions/experimentalshields=unchanged	game/modoptions/tweakunits5=	game/modoptions/experimentallegionfaction=0	game/modoptions/multiplier_buildpower=1	game/modoptions/scavspawnarea=1	game/modoptions/teamcolors_anonymous_mode=0	game/modoptions/lootboxes=scav_only	game/modoptions/tweakdefs2=	game/modoptions/chicken_chickenstart=initialbox	game/modoptions/scoremode_chess_spawnsperphase=1	game/modoptions/tweakunits2=	game/modoptions/scavbosshealth=1	game/modoptions/multiplier_weapondamage=1	game/modoptions/map_waterlevel=0	game/modoptions/unit_restrictions_nonukes=0	game/modoptions/usemexconfig=0	game/modoptions/tweakunits=	game/modoptions/scavgraceperiod=5	game/modoptions/multiplier_buildtimecost=1	game/modoptions/numberofcontrolpoints=13	game/modoptions/ffa_mode=0	game/modoptions/chicken_queentime=40	game/modoptions/unit_restrictions_notacnukes=0	game/modoptions/chicken_graceperiod=5	game/modoptions/experimentalrebalancet2labs=0	game/modoptions/transportenemy=notcoms	game/modoptions/tweakdefs7=	game/modoptions/scavconstructors=1	game/modoptions/scavbuildspeedmultiplier=1	game/modoptions/tweakunits9=	game/hosttype=SPADS	game/modoptions/multiplier_energycost=1	game/modoptions/unit_restrictions_noextractors=0	game/modoptions/commanderbuildersbuildpower=500	game/modoptions/tweakunits4=	game/modoptions/shareddynamicalliancevictory=0	game/modoptions/scavunitveterancymultiplier=1	game/modoptions/ruins=scav_only	game/modoptions/teamcolors_icon_dev_mode=disabled	game/modoptions/tweakdefs9=	game/modoptions/multiplier_metalcost=1	game/modoptions/multiplier_weaponrange=1	game/modoptions/scoremode=disabled	game/modoptions/dominationscoretime=30	game/modoptions/capturetime=30	game/modoptions/scavendless=0	game/modoptions/multiplier_builddistance=1	game/modoptions/experimentalflankingbonusmax=190	game/modoptions/ffa_wreckage=0	game/modoptions/experimentalrebalancehovercrafttech=1	game/modoptions/experimentalmassoverride=0	game/modoptions/map_tidal=unchanged	game/modoptions/deathmode=com	game/modoptions/tweakdefs8=	game/modoptions/experimentalflankingbonusmode=1	game/modoptions/multiplier_turnrate=1	game/modoptions/maxunits=2000	game/modoptions/unit_restrictions_notech3=0	game/startpostype=2	game/modoptions/multiplier_maxdamage=1	game/modoptions/usemapconfig=1	game/modoptions/scavstartboxcloud=1	game/modoptions/experimentalflankingbonusmin=90\n")
                bar_socket.send_message(
                    sock, "CLIENTBATTLESTATUS %s 4194306 16777215\n" % USERNAME)
            elif "REQUESTBATTLESTATUS" in message:
                bar_socket.send_message(sock, "MYBATTLESTATUS 4195330 0\n")
                bar_socket.send_message(sock, "SAYBATTLE Hello there!\n")
                bar_socket.send_message(
                    sock, "SAYBATTLEEX * BarManager|{\"BattleStateChanged\": {\"locked\": \"unlocked\", \"autoBalance\": \"advanced\", \"teamSize\": \"8\", \"nbTeams\": \"2\", \"balanceMode\": \"clan;skill\", \"preset\": \"team\"}}\n")
                bar_socket.send_message(
                    sock, "SAYBATTLEEX * Boss mode enabled for 2late\n")
            # elif "UPDATEBATTLEINFO" in message:
            #     bar_socket.send_message(
            #         sock, "JOINBATTLE %s empty sPassword\n" % battle_id)
            elif "JOINBATTLEREQUEST" in message:
                username = message.split(" ")[1]
                bar_socket.send_message(
                    sock, "JOINBATTLEACCEPT %s\n" % username)
            elif "JOINEDBATTLE" in message:
                print("Joined battle")


battle_thread = threading.Thread(target=create_battle)
battle_thread.start()

while True:
    cmd = input()
    bar_socket.send_message(sock, cmd + "\n")
