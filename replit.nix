{pkgs}: {
  deps = [
    pkgs.geckodriver
    pkgs.wget
    pkgs.zlib
    pkgs.xcodebuild
    pkgs.chromium
    pkgs.chromedriver
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.zlib
    ];
  };
}
