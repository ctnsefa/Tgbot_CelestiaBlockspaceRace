# Celestia-Blockspacerace - Telegram Bot for the PayForBlob transactions
## Description
Create any useful tool, whether it is a command-line application or a dashboard tooling, that will be a net-benefit for the Celestia network, whether for validators, node operators, or developers.(https://docs.celestia.org/nodes/itn-toolings/) <br/> <br/>
#### For deploy the light-node automatically
```
wget -O auto-install-light-node.sh https://raw.githubusercontent.com/owlstake/celestia-race/main/deploy-light-node/auto-install-light-node.sh && chmod +x auto-install-light-node.sh && ./auto-install-light-node.sh
```
### How to work ?
#### 1-First of all, we go into the server where we set up the Celestia light node and stop the node. <br/> <br/>
`systemctl disable celestia-lightd` <br/>
`systemctl stop celestia-lightd` <br/> <br/>
#### 2- Create service <br/> <br/>
```
sudo tee <<EOF >/dev/null /etc/systemd/system/celestia-lightd.service
[Unit]
Description=celestia-lightd Light Node
After=network-online.target

[Service]
User=$USER
ExecStart=/usr/local/bin/celestia light start --core.ip https://api-blockspacerace.pops.one/ --core.rpc.port 26657 --core.grpc.port 9090 --keyring.accname my_celes_key --metrics.tls=false --metrics --metrics.endpoint otel.celestia.tools:4318 --gateway --gateway.addr 0.0.0.0 --gateway.port 26659 --p2p.network blockspacerace
Restart=on-failure
RestartSec=3
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
EOF
``` 
#### 3-Start node <br/> <br/>
`systemctl enable celestia-lightd` <br/>
`systemctl start celestia-lightd` <br/> <br/>
#### 4-Check logs <br/>
`journalctl -u celestia-lightd.service -f` <br/> <br/>
#### 5-Install Python and Flask <br/>
```
pip install flask
pip install python-telegram-bot

```
#### 6-Create directories <br/>
```
mkdir pfb  
cd 
mv app.py pfb/ 

```
## NOTE: app.py contents are shared in repo as open source.Please check. <br/> <br/>
#### 7-To start <br/>
```
cd pfb
python3 app.py
```
#### Start and use. <br/> <br/>
#### Don't forget to open the port! :26659 <br/> <br/>
# TELEGRAM BOT ADRESS : - https://web.telegram.org/k/#@pfb12_bot
 <br/> <br/>
## Give the bot a /start command and enter the NODE IP ADDRESS. <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace-telegrambot/main/start_bot.png" width="auto"> <br/> <br/>
## And it should output this . <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace-telegrambot/main/txhash_bot.png"> <br/> <br/>
## After entering /explorer command, explorer will exit and you can check txhash. <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace-telegrambot/main/explorer_bot.png"> <br/> <br/>
## And the result is successful <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace-telegrambot/main/success.png"> <br/> <br/>
