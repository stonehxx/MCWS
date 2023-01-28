import json

def send():
    DATA = {}
    DATA["hander"] = hander()
    DATA["body"] = body()
    return DATA

def hander():
    return ""

def body():
    return ""

class API():
    def is_event(self,recv_data):
        return recv_data['header']['messagePurpose']=='event'
    def is_playerchat(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerMessage' and recv_data['body']['properties']['MessageType']=='chat'
    def is_playersay(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerMessage' and recv_data['body']['properties']['MessageType']=='say'
    def is_playertell(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerMessage' and recv_data['body']['properties']['MessageType']=='say'
    def is_block_broken(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='BlockBroken'
    def is_block_placed(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='BlockPlaced'
    def is_player_join(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerJoin'
    def is_player_leave(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerLeave'
    def is_portal_built(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PortalBuilt'
    def is_portal_used(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PortalUsed'
    def is_player_died(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='PlayerDied'
    def is_mob_killed(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='MobKilled'
    def is_item_destroyed(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='ItemDestroyed'
    def is_item_crafted(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='ItemCrafted'
    def is_boss_killed(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='BossKilled'
    def is_agent_command(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='AgentCommand'
    def is_agent_created(self,recv_data):
        return False if not self.is_event(recv_data) else recv_data['body']['eventName']=='AgentCreated'
    def is_command_response(self,recv_data):
        return recv_data['header']['messagePurpose']=='commandResponse'
    def get_pkg_data(self,recv_data):
        if self.is_playerchat(recv_data) or self.is_playersay(recv_data):
            return [recv_data['body']['properties']['Sender'],recv_data['body']['properties']['Message']]
        elif self.is_playertell(recv_data):
            return [recv_data['body']['properties']['Sender'],recv_data['body']['properties']['Receiver'],recv_data['body']['properties']['Message']]
        elif self.is_block_broken(recv_data):
            return [recv_data['body']['properties']['Block'],recv_data['body']['properties']['Type'],recv_data['body']['properties']['ToolItemType']]
        elif self.is_block_placed(recv_data):
            return [recv_data['body']['properties']['Block'],recv_data['body']['properties']['Type']]
        elif self.is_player_join(recv_data) or self.is_player_leave(recv_data):
            return [recv_data['body']['properties']['PlayerName'],recv_data['body']['properties']['PlayerColor']]
        elif self.is_player_died(recv_data):
            return [recv_data['body']['properties']['Cause'],recv_data['body']['properties']['KillerEntity']]
        elif self.is_mob_killed(recv_data):
            return [recv_data['body']['properties']['MobType'],recv_data['body']['properties']['WeaponType']]
        elif self.is_item_destroyed(recv_data):
            return recv_data['body']['properties']['DestructionMethodType']
        elif self.is_boss_killed(recv_data):
            return recv_data['body']['properties']['BossType']
        elif self.is_command_response(recv_data):
            return [recv_data['body']['statusCode'],recv_data['body'].get('statusMessage')]
    def get_subscribe_list(self):
        return ["WorldUnloaded","BlockBroken","BlockPlaced","BoardTextUpdated","AgentCreated","AgentCommand","BossKilled","ItemCrafted","ItemDestroyed","ItemUsed","MobKilled","PlayerDied","PlayerJoin","PlayerLeave","PlayerTeleported","PortalBuilt","PortalUsed","PlayerMessage"]
    def get_pkg_subscribe(self,eventName):
        out=[]
        for x in eventName:
            out.append(json.dumps({
                "body": {
                "eventName": x
                    },
                "header": {
                    "requestId": "00000000-0000-0000-0000-000000000000",
                    "messagePurpose": "subscribe",
                    "version": 1,
                    "messageType": "commandRequest"
                    }
                }))
        return out
    def get_pkg_command(self,command):
        return json.dumps({
            "body": {
                "origin": {
                    "type": "player"
                    },
                "commandLine":command,
                "version": 1
                },
            "header": {
                "requestId": "00000000-0000-0000-0000-990000000001",
                "messagePurpose": "commandRequest",
                "version": 1,
                "messageType": "commandRequest"
                }
            })