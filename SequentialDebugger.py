#insert into nn.Sequential to print tensor shape
class debug(nn.Module):
    def __init(self):
        super(debug, self).__init__()
    def forward(self, x):
        print(x.shape)
        return x