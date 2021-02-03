# -*- encoding: utf8 -*-
class CustomBase64(object):
    comparison = {
            "0":"A", "8":  "I","16":"Q","24":"Y","32":"g","40":"o","48":"w","56":"4",
            "1":"B", "9":	"J","17":"R","25":"Z","33":"h","41":"p","49":"x","57":"5",
            "2":"C", "10":	"K","18":"S","26":"a","34":"i","42":"q","50":"y","58":"6",
            "3":"D", "11":	"L","19":"T","27":"b","35":"j","43":"r","51":"z","59":"7",
            "4":"E", "12":	"M","20":"U","28":"c","36":"k","44":"s","52":"0","60":"8",
            "5":"F", "13":	"N","21":"V","29":"d","37":"l","45":"t","53":"1","61":"9",
            "6":"G", "14":	"O","22":"W","30":"e","38":"m","46":"u","54":"2","62":"+",
            "7":"H", "15":	"P","23":"X","31":"f","39":"n","47":"v","55":"3","63":"/",
            "65": "="
            }

    def encode(self, value, threshold):
        value = "".join(['0' + bin(ord(i))[2:] for i in value])
        inputs = self.shift(value, threshold)
        result = ''
        for i in inputs:
            if i == '0' * threshold:
                # 如果全部为0，进行补位
                encoding = 65
            else:
                encoding = 0
                for index, v in enumerate(i[::-1]):
                    val = int(v) * pow(2, index)
                    encoding += val
            after = self.comparison.get(str(encoding))
            result += after
        return result

    def decode(self, value, threshold, group=8):
        result = []
        coder = self.str2binary(value, threshold)
        bins = self.shift(''.join(coder), group)
        for i in range(len(bins)):
            binary = ''.join(bins)[i * group: (i + 1) * group]
            if binary != '0' * group:
                result.append("".join([chr(i) for i  in [int(b, 2) for b in binary.split(" ")]]))

        return ''.join(result)

    def str2binary(self, value, threshold):
        result = []
        values = self.str2decimal(value)
        for i in values:
            if i == '65':
                val = '0' * threshold
            else:
                val = '{:0{threshold}b}'.format(int(i), threshold=threshold)
                print i, threshold, val
            result.append(val)
        return result

    def str2decimal(self, value):
        """str 转Base64 码表十进制"""
        keys = []
        for t in value:
            for index, value in self.comparison.items():
                if value == t:
                     keys.append(index)
        return keys

    @staticmethod
    def shift(value, threshold, group=24):
        """位数转换"""
        remainder = len(value) % group
        if remainder:
            # 如有余数，说明需要用0补位
            padding = '0' * (group - remainder)
            value += padding

        # 按着threshold 值切割字符
        result = [value[i: i + threshold] for i in range(0, len(value), threshold)]
        return result


if __name__ == "__main__":
    cus = CustomBase64()
    encode_res = cus.encode("async", threshold=6)
    print encode_res
    decode_res = cus.decode(encode_res, threshold=6)
    print decode_res