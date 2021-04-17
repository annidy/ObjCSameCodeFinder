//
//  MachoReader.m
//  MachoRenamer
//
//  Created by annidy on 16/7/31.
//  Copyright © 2016年 annidy. All rights reserved.
//

#import "MachoFile.h"
#import "NSFileHandle+Block.h"

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

- (void)setMachoFile:(NSString *)machoFile {
    if (_machoFile != machoFile) {
        _machoFile = [machoFile copy];
        [self load];
    }
}


@end
