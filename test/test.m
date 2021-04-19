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


@end