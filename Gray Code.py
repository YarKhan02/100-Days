def gray_code():
    n = int(input())

    if (n <= 0):
        return
    
    my_list = list()
    my_list.append("0")
    my_list.append("1")
    i = 2
    j = 0
    
    while(True):
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            my_list.append(my_list[j])
        for j in range(i):
            my_list[j] = "0" + my_list[j]
        for j in range(i, 2 * i):
            my_list[j] = "1" + my_list[j]
        
        i = i << 1
    
    for i in range(len(my_list)):
        print(my_list[i])

    return ''


print(gray_code())

# def gray_code(n):

#     if n == 0:
#         return '00'
#     if n == 1:
#         return '01'

#     res = gray_code(n - 1)

#     print(['0' + s for s in res] + ['1' + s for s in res[::-1]])


# int main() {
#     int n;
#     cin >> n;
#     vector<string> gray_code;
#     gray_code.push_back("");
#     for (int i = 0; i < n; i++) {
#         int size = gray_code.size();
#         for (int j = size - 1; j >= 0; j--) {
#             gray_code.push_back(gray_code[j]);
#         }
#         size *= 2;
#         for (int j = 0; j < size; j++) {
#             if (j < gray_code.size() / 2) {
#                 gray_code[j] += "0";
#             } else {
#                 gray_code[j] += "1";
#             }
#         }
#     }
#     for (int i = 0; i < gray_code.size(); i++) {
#         cout << gray_code[i] << endl;
#     }
# }