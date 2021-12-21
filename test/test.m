@implementation MachoFile
{
    NSFileHandle *_fileHandle;
}

- (instancetype)initWithPath:(NSString *)file {
    self = [super init];
    if (self) {
        self.machoFile = file;
    }
    return self;
}

+ (instancetype)initWithPath:(NSString *)file {
    self = [super init];
    if (self) {
        self.machoFile = file;
    }
    self = [super init];
    if (self) {
        self.machoFile = file;
    }
    return self;
}

+ (instancetype)initWithPath:(NSString *)file {
//     self = [super init];
//     if (self) {} badcase
        self.machoFile = file;
//     }
    return self;
}

@end
