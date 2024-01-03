import unittest

from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl


class TestResponseGenerator(unittest.TestCase):

    def testBoolTypeResponse(self):
        # Booltype은 다 처리 가능 확인
        # 1, 3, 4, 6, 8, 9, 10, 13
        sampleResponse = {"protocolNumber": 4, "data": True}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        print(response.getIsSuccess())

    def testDictionaryResponse(self):
        # 2, 7, 12
        # sampleResponse = {"protocolNumber": 7, "data": {'__productId': 1, '__productName': "Sibal",
        #                                                 "__productPrice": 20000, "__productDetails": "Dog Sibal",
        #                                                 '__seller': "m.e"}}
        sampleResponse = {"protocolNumber": 2, "data": {"__accountSessionId": 10}}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        # print(response.getId())
        # print(response.getName())
        # print(response.getPrice())
        # print(response.getDetails())
        # print(response.getAccountId())
        print(response.getAccountSessionId())

    def testListResponse(self):
        # 5, 11
        sampleResponse = {"protocolNumber": 5, "data": [{'__productId': 1, '__productName': "Sibal",
                                                         "__productPrice": 20000},
                                                        {'__productId': 2, '__productName': "Sibal",
                                                         "__productPrice": 30000},
                                                        {'__productId': 3, '__productName': "Sibal",
                                                         "__productPrice": 1818}]}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        # myOrderList = response.getMyOrderList()
        # myOrderListLength = len(myOrderList)
        # print(myOrderListLength)
        # for i in range(myOrderListLength):
        #     print(myOrderList[i])

        productList = response.getProductList()
        productListLength = len(productList)
        # print(productListLength)
        for i in range(productListLength):
            # print(productList[i])
            print(receivedData[i]["__productId"], "      ", receivedData[i]["__productName"], "      ",
                  receivedData[i]["__productPrice"], "원")


if __name__ == '__main__':
    unittest.main()
