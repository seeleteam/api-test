# api-test
This repository aims to test [go-seele](https://github.com/seeleteam/go-seele). basically it includes the following three types of testing.

* ![](http://progressed.io/bar/50?title=http-api)
* ![](http://progressed.io/bar/0?title=ws-api)
* ![](http://progressed.io/bar/0?title=tcp-api)
* ![](http://progressed.io/bar/100?title=cli-api)

An independent reporisity for [cli-api](https://github.com/seeleteam/e2e-blackbox). it's name is  *e2e-blackbox*.


### Prepare your environment

	virtualenv ~/testEnv
	source ~/testEnv
	pip install -r requirements.txt



### Manual testing

Simply test me


    py.test http/test_*


Generates a HTML report for the test results

    py.test --html=report.html http/test_*

### Automation testing

to notice developer as soon as test finished. you should set your email.


    export MAIL_ADDR=<your-email@xxx.com>
    export MAIL_PASSWD=<your-email-password>

### Run on docker

	docker build -t my-test-server .
	docker run -it --rm --name my-running-app my-test-server
	# or run it in daemon mode
	docker run -d --rm --name my-running-app my-test-server
	

### How to trigger

To fire up your test case, there are three way to reach that.

* scheduler job
* monitor the commit of the reporisity by developer.
* manual trigger


### API's List

| HTTP | WS | TCP | CLI| Status|
|------|----|-----|----|-------|
| seele_getInfo | -| -| getinfo| ✔︎ |
| seele_getAccountNonce| -| -| getnonce|
| seele_getBlockHeight| - | -| getblockheight| ✔︎ |
| seele_getBlock| - | -| getblock| ✔︎ |
| seele_call| - | -| call| ✔︎ |
| seele_getBlockByHeight|-|-|-| ✔︎ |
| seele_getBlockByHash|-|-| getdebtbyhash|✔︎ |
| monitor_nodeInfo|-|-|getinfo|✔︎ |
| monitor_nodeStats|-|-|-|✔︎ |
| seele_getBalance|-|-|getbalance|✔︎ |


### Deprecated API

* debug_getTPS
* debug_dumpHeap
* network_getProtocolVersion
* network_getPeersInfo
* network_getPeerCount
* network_getNetVersion
* network_getNetworkID
* miner_start
* miner_stop
* miner_status
* miner.GetCoinbase
* miner_setThreads
* miner_setcoinbase
* miner_getEngineInfo
* debug_printBlock
* debug_getTxPoolContent
* debug_getTxPoolTxCount
* debug_getPendingTransactions
* debug_getPendingDebts
* debug_dumpHeap
* download_getStatus

 

### Hard to test API

* seele_addTx
* 
